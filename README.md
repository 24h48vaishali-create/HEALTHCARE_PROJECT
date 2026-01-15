# Web-Based Emergency Healthcare Information System

## Project Overview

The Emergency Healthcare Information System is a web-based application that helps users quickly identify nearby hospitals offering required emergency medical services. The system provides real-time information about hospital facilities and doctor availability to reduce delays during critical medical situations.

---

## Description of Problem Statement
During medical emergencies, patients and their families often face difficulty in identifying the right hospital that provides the required emergency treatment. Lack of centralized and real-time information leads to wasted time, confusion, and delayed medical care, which can be life-threatening.

---

## Solution Overview
This project provides a centralized web platform where users can search for nearby hospitals based on emergency type and location. Hospitals update their emergency service availability, ensuring that users receive accurate and up-to-date information. The system helps patients reach the correct hospital without unnecessary delays.

---

## Key Features
* Emergency-based hospital search
  
* Location-based nearby hospital listing
  
* Real-time availability of emergency services
  
* Doctor and specialist availability view
  
* Hospital registration and service updates
  
* Simple and fast user interface for emergencies

---

## Tech Stack
* Frontend:Vanilla JS(HTML+CSS+Javascript)
  
* Backend-Python(programming language),Flask (Web Framework)

* Database:SQLite
   
* Deployment:Render

*Tools & Environment:
  1. Git & GitHub  
  2.VS Code  
  3.pip (Python Package Manager) 

---

## Project Structure:
---
HEALTHCARE_PROJECT/
│── app.py
│── requirements.txt
│── database.py
│── routes.py
│── admin_routes.py
│
├── templates/
│ ├── index.html
│ ├── admin.html
│
├── static/
│ ├── style.css
│ └── script.js
│
├── README.md
└── .gitignore

---
---

## Installation and Setup:
Follow the steps below to run the project locally.

---

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git
- Any modern web browser

---

## Clone the Repository

Open terminal or Git Bash and run:

git clone https://github.com/24h48vaishali-create/HEALTHCARE_PROJECT.git

Then move into the project folder:

cd HEALTHCARE_PROJECT

---

## Create a Virtual Environment

Create virtual environment:

python -m venv venv

Activate it:

Windows:
venv\Scripts\activate

---

## Install Required Dependencies

Install dependencies:

pip install -r requirements.txt

If that fails, run:

pip install flask

---

## Run the Application

Start the Flask server:

python app.py

You should see something like:

Running on http://127.0.0.1:5000/

---

## Open in Browser

Open your browser and go to:

http://127.0.0.1:5000/

---

## Stop the Server

Press CTRL + C in the terminal to stop the server.

---

## Usage

* Open the application in your web browser.
* Search hospitals based on emergency type and location.
* View nearby hospitals with available emergency services.
* Hospitals/Admin can update service and doctor availability.
* All updates are reflected in real time.

---

## Future Enhancements

* SMS/Email emergency alerts.
* Mobile application support.
* Integration with government and public healthcare databases.
* Role-based authentication and authorization system to provide separate access levels for administrators, hospitals, and doctors, ensuring secure and controlled data updates.


---

## Team Contributors

* Vaishali Kolpe
* Tanish Dinesh Purusha
* Shaun Joshua Sequeira
* Shravya G

---

## License

This project is licensed under the MIT License.
