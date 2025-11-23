from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "portfolio_secret_key"

# Portfolio Data
portfolio = {
    "name": "Maddi Akhil",
    "role": "Python Developer Intern",
    "profile": "A motivated and curious Computer Science student with hands-on experience in backend development. Continuously learning full-stack development, including HTML, CSS, JavaScript, and React.js.",
    "contact": {
        "email": "akhilmaddi2004@gmail.com",
        "phone": "+91-7995859338",
        "linkedin": "https://www.linkedin.com/in/akhil-maddi-a2k4",
        "github": "https://github.com/akhilmaddi2004"
    },
    "education": [
        {"degree": "B.Tech in Computer Science and Engineering", "institute": "Trinity College of Engineering and Technology, Karimnagar", "year": "Expected 2026"},
        {"degree": "Intermediate (MPC)", "institute": "Government Junior College Boys, Siddipet", "year": "Completed 2022"},
        {"degree": "Secondary School (SSC)", "institute": "Sri Vani High School, Siddipet", "year": "Completed 2020"}
    ],
    "experience": [
        {"role": "Web Design Intern", "company": "Sparks to Ideas", "duration": "Apr 2025 – May 2025", "details": ["Designed responsive webpages using HTML, CSS, Bootstrap 5", "Applied animations and jQuery effects", "Learned cross-browser compatibility and layout design"]}
    ],
    "skills": ["Python", "HTML", "CSS", "JavaScript", "Flask", "MySQL", "React.js (learning)", "Bootstrap 5", "REST APIs", "CRUD operations", "OOP", "Responsive Design"],
    "projects": [
        {"name": "IoT-Based Real-Time Health Monitoring System", "description": "Monitored temperature and heart rate using Arduino, sensors, and LCD.", "link": "https://github.com/akhilmaddi2004"},
        {"name": "Kidney Disease Prediction (ML)", "description": "Built ML model to predict kidney disease using Python, Pandas, Scikit-learn.", "link": "https://github.com/akhilmaddi2004"},
        {"name": "Calculator CLI App", "description": "Created a command-line Python calculator for basic operations.", "link": "https://github.com/akhilmaddi2004"},
        {"name": "To-Do List Application", "description": "Implemented a console-based to-do list manager in Python.", "link": "https://github.com/akhilmaddi2004"},
        {"name": "Web Scraper for News Headlines", "description": "Scraped top headlines using Python, requests, BeautifulSoup.", "link": "https://github.com/akhilmaddi2004"},
        {"name": "REST API with Flask", "description": "Developed a Flask API with GET/POST/PUT/DELETE routes to manage users.", "link": "https://github.com/akhilmaddi2004"},
        {"name": "Data Analysis on CSV Files", "description": "Analyzed sales data using Pandas and generated charts in Jupyter Notebook.", "link": "https://github.com/akhilmaddi2004"}
    ]
}

@app.route('/')
def index():
    return render_template("index.html", portfolio=portfolio)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        # In a real app, you would send an email here.
        # For the internship task, flash message is perfect.
        flash(f"Thanks {name}! I'll get back to you soon.")
        return redirect(url_for("contact"))
    return render_template("contact.html", portfolio=portfolio)

if __name__ == "__main__":
    # use_reloader=False prevents the infinite loop/crash on OneDrive
    app.run(debug=True, use_reloader=False)