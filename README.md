# 🐍 Flask Professional Portfolio

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-red?style=for-the-badge&logo=flask&logoColor=white)
![Frontend](https://img.shields.io/badge/HTML5%20%26%20CSS3-Modern-green?style=for-the-badge)

> **Python Developer Internship - Task 6**
>
> A dynamic, fully responsive personal portfolio website built using the Flask micro-framework. This project demonstrates the use of **Flask Routes**, **Jinja2 Templating**, and **Modern CSS Design** to create a professional digital presence.

---

## 🎥 Project Walkthrough / Screen Recording

I have recorded a full walkthrough of the website running locally via VS Code to demonstrate the animations, responsiveness, and routing.

**### [▶️ Click Here to Watch the Demo Video](https://github.com/akhilmaddi2004/flask-professional-portfolio-6/blob/main/portfolio_flask_6/videos/demo%20(1).mp4)**
> `[Link to demo.mp4 file inside the repo]`

---

## 🚀 Key Features

* **Dynamic Content Rendering:** All portfolio data (Skills, Projects, Experience) is stored in Python dictionaries in `app.py` and dynamically rendered using **Jinja2 loops**.
* **Modern UI/UX:**
    * **"Dark Tech" Theme:** Professional dark navy background with neon accents (`#0f172a` & `#38bdf8`).
    * **Glassmorphism:** Translucent card effects for projects and experience.
    * **Responsive Design:** Fully optimized for Desktop, Tablet, and Mobile devices.
* **Split-Hero Layout:** Modern layout with profile image on the left and introduction on the right.
* **Contact Form Logic:** Implemented `POST` method handling with Flask `flash` messaging for user feedback.

---

## 🛠️ Tech Stack Used

| Component | Technology | Usage |
| :--- | :--- | :--- |
| **Backend** | ![Python](https://img.shields.io/badge/-Python-black?logo=python) | Core logic and data structures |
| **Framework** | ![Flask](https://img.shields.io/badge/-Flask-black?logo=flask) | Routing, Server, and Request handling |
| **Templating** | **Jinja2** | Rendering HTML dynamically with Python data |
| **Styling** | **CSS3 (Custom)** | Animations, Grid/Flexbox layouts, Dark Mode |
| **Frontend** | **HTML5** | Semantic structure |

---

## 📂 Folder Structure

```text
portfolio-flask/
│
├── app.py              # Main Flask application (Routes & Data)
├── requirements.txt    # Dependencies
├── README.md           # Documentation
│
├── static/             # Static Assets (CSS, Images)
│   ├── style.css       # Custom Styling
│   └── images/
│       └── profile.png # Profile Picture
│
└── templates/          # HTML Templates
    ├── index.html      # Main Portfolio Page
    └── contact.html    # Contact Form Page
⚙️ How to Run Locally
Follow these steps to run the portfolio on your machine:

Clone the Repository

Bash

git clone [https://github.com/akhilmaddi2004/flask-professional-portfolio.git](https://github.com/akhilmaddi2004/flask-professional-portfolio.git)
cd flask-professional-portfolio
Install Dependencies

Bash

pip install -r requirements.txt
Run the Application

Bash

python app.py
View in Browser Open your browser and go to: http://127.0.0.1:5000

📝 Internship Task Details
Task 6: Build a Portfolio Website with Flask

Objective: Create a personal portfolio site.

Tools: Python, Flask, HTML, CSS.

Deliverables: A Flask project folder demonstrating Routing, Templates, and Forms.

📬 Contact
Maddi Akhil

GitHub: github.com/akhilmaddi2004

LinkedIn: linkedin.com/in/akhil-maddi-a2k4

Email: akhilmaddi2004@gmail.com

Built with ❤️ for the Python Developer Internship.
