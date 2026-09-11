# 🖼️ End-to-End Image Scraping Tool

<p style="font-family: 'Times New Roman', Times, serif; font-weight: bold; font-style: italic;">

🚨 Points to keep in sight before accessing the execution video are as follows:

<br>

1. The project schema contains several folders. Among them, there is a folder named "images".

<br>

2. The folder "images" initially contains no media before the command is given to the image scraping tool.

<br>

3. After the command is given, a number of media files can be seen in the "images" folder. This action confirms that the tool has performed the required actions successfully.

</p>

https://github.com/user-attachments/assets/2c965410-9235-4ade-aec2-211d35372d3e




<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,14,16,18&height=220&section=header&text=Image%20Scraping%20Tool&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=35"/>
</p>

<p align="center">
  <b>A Flask-based web application for searching and downloading images through an easy-to-use interface.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-000000?style=for-the-badge&logo=flask&logoColor=white"/>
  <img src="https://img.shields.io/badge/BeautifulSoup-Web%20Scraping-4B8BBE?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Requests-HTTP%20Requests-FF6F00?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/PyMongo-MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white"/>
</p>

---

## 📌 About the Project

The **Image Scraping Tool** is a Flask web application that allows users to search for images and download them directly to their local machines.

The application uses web-scraping techniques to retrieve image URLs from search results and provides a convenient way to collect images based on a particular search query.

### 🎯 Motivation

Images are widely used in:

* 🌐 Web Development
* 📊 Data Analysis
* 🤖 Machine Learning
* 🎨 Content Creation
* 📚 Research & Education

Collecting a large number of images manually can be time-consuming. This project aims to simplify that process by providing a user-friendly interface through which users can search for images and retrieve them without manually visiting multiple websites and downloading images individually.

---

## ✨ Features

* 🔍 Search for images using a keyword
* 🌐 Fetch image URLs through web scraping
* ⬇️ Download images directly to the local machine
* 🖥️ Simple Flask-based web interface
* 🐍 Python-based implementation
* 🗄️ MongoDB connectivity through PyMongo
* ⚡ Automated image collection workflow

---

## 🛠️ Tech Stack

| Technology        | Purpose                     |
| ----------------- | --------------------------- |
| 🐍 Python         | Core programming language   |
| 🌐 Flask          | Web application framework   |
| 🔎 Beautiful Soup | HTML parsing & web scraping |
| 📡 Requests       | Sending HTTP requests       |
| 🗄️ PyMongo       | MongoDB connectivity        |
| 🍃 MongoDB        | Database support            |

---

## 📦 Dependencies & Requirements

The project requires the following Python libraries:

```text
Flask
Requests
BeautifulSoup
PyMongo
```

All required dependencies can be installed using the project's `requirements.txt` file.

```bash
pip install -r requirements.txt
```

---

## 📂 Project Workflow

```text
                 🔍 SEARCH QUERY
                       │
                       ▼
              ┌─────────────────┐
              │   Flask Web App │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Search Results │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Beautiful Soup  │
              │  HTML Parsing   │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Extract Image  │
              │      URLs       │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Download Images │
              └────────┬────────┘
                       │
                       ▼
                💾 LOCAL STORAGE
```

---

## 🚀 Project Execution

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/keshavkapill/IMAGE-SCRAPPING-TOOL.git
```

Move into the project directory:

```bash
cd IMAGE-SCRAPPING-TOOL
```

---

### 2️⃣ Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the Application

Execute the Flask application:

```bash
python app.py
```

The application can then be accessed through the local Flask server displayed in the terminal.

---

## 🖼️ Application Preview

If your project contains the original screenshot, you can keep it here:

```markdown
![Image Scraping Tool](static/css/Screenshot%202023-08-03%20214154.png)
```

> Keep your existing screenshot path if the image is already present in your repository.

---

## 🧠 What This Project Demonstrates

This project provides practical exposure to:

* Python web development
* Flask application development
* Web scraping
* HTML parsing
* HTTP requests
* Image URL extraction
* Automated file downloading
* MongoDB connectivity
* Backend application workflow

---

## 🔮 Future Improvements

Some possible improvements for the project include:

* 📸 Support for multiple search engines
* 🎨 Improved user interface
* 🔢 User-defined image download limits
* 🗂️ Automatic image categorization
* 🏷️ Image metadata extraction
* 🖼️ Image preview before downloading
* 📁 Custom download directories
* ⚡ Improved scraping performance
* 🔐 Better error handling and validation

---

## 👨‍💻 Developer

### Keshav Kapil

Built with ❤️ by **Keshav Kapil**

<p align="center">

<a href="https://github.com/keshavkapill">
<img src="https://img.shields.io/badge/GitHub-Keshav%20Kapil-181717?style=for-the-badge&logo=github&logoColor=white"/>
</a>

<a href="https://www.linkedin.com/in/keshavkapil15/">
<img src="https://img.shields.io/badge/LinkedIn-Keshav%20Kapil-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>

</p>

---

<p align="center">
  <b>Made with ❤️ by Keshav Kapil</b>
</p>

<p align="center">
  <a href="https://github.com/keshavkapill">GitHub</a>
  &nbsp;•&nbsp;
  <a href="https://www.linkedin.com/in/keshavkapil15/">LinkedIn</a>
</p>
