from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup
import logging
import pymongo
import os
import re

logging.basicConfig(filename="scrapper.log", level=logging.INFO)

app = Flask(__name__)


def fetch_image_urls(query, max_urls=10):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    urls = []

    # 1. Bing Images direct links (murl)
    try:
        bing_url = f"https://www.bing.com/images/search?q={query}"
        res = requests.get(bing_url, headers=headers, timeout=10)
        murls = re.findall(r'&quot;murl&quot;:&quot;(http[^&]+)&quot;', res.text)
        urls.extend(murls)
    except Exception as e:
        logging.info(f"Bing scrape error: {e}")

    # 2. Fallback to Google img tags
    if not urls:
        try:
            g_url = f"https://www.google.com/search?q={query}&tbm=isch"
            res_g = requests.get(g_url, headers=headers, timeout=10)
            soup = BeautifulSoup(res_g.content, "html.parser")
            for img in soup.find_all("img"):
                src = img.get("src") or img.get("data-src")
                if src and src.startswith("http"):
                    urls.append(src)
        except Exception as e:
            logging.info(f"Google scrape error: {e}")

    # Deduplicate while preserving order
    seen = set()
    deduped = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            deduped.append(u)

    return deduped[:max_urls]


@app.route("/", methods=['GET'])
def homepage():
    return render_template("index.html")


@app.route("/review", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            query = request.form['content'].replace(" ", "")
            if not query:
                return "Please enter a valid search query!"

            save_directory = "images/"
            if not os.path.exists(save_directory):
                os.makedirs(save_directory)

            image_urls = fetch_image_urls(query, max_urls=10)
            if not image_urls:
                return "No images found for your query, please try another search term."

            img_data = []
            download_count = 0
            for idx, image_url in enumerate(image_urls):
                try:
                    img_bytes = requests.get(image_url, timeout=5).content
                    if img_bytes:
                        mydict = {"Index": idx, "Image": img_bytes}
                        img_data.append(mydict)
                        file_path = os.path.join(save_directory, f"{query}_{idx}.jpg")
                        with open(file_path, "wb") as f:
                            f.write(img_bytes)
                        download_count += 1
                except Exception as img_err:
                    logging.info(f"Failed to download image {idx}: {img_err}")

            # Optional MongoDB storage
            try:
                client = pymongo.MongoClient("mongodb+srv://kalyanmurapaka274:<password>@ineuron.3uqntxj.mongodb.net/?retryWrites=true&w=majority")
                db = client['image_scrap']
                review_col = db['image_scrap_data']
                if img_data:
                    review_col.insert_many(img_data)
            except Exception as db_err:
                logging.info(f"MongoDB saving skipped: {db_err}")

            return f"Images downloaded successfully! {download_count} images saved to your 'images/' folder."
        except Exception as e:
            logging.exception("Error during scraping:")
            return 'Something went wrong while scraping images, please try again!'

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
