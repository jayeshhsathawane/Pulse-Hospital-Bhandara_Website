# 🏥 Pulse Multispeciality Hospital Management System

A professional Hospital Management System built with Django. This platform handles patient appointments and provides a secure dashboard for doctors to manage consultations and digital prescriptions.
---
## ✨ Features

* **Patient Appointment System:** Simple and intuitive form for patients to book visits.
* **Doctor Dashboard:** Secure login for doctors to view daily patient queues and history.
* **Digital Prescriptions:** Create and manage patient diagnoses and medications.
* **Print-Ready Reports:** Prescriptions are optimized for professional printing on hospital letterheads.
* **Secure Configuration:** Uses environment variables (.env) to protect sensitive data like Secret Keys.

---

## 🛠️ Tech Stack
* **Backend:** Python 3.x, Django 4.x
* **Environment Management:** python-dotenv
* **Frontend:** HTML5, CSS3, JavaScript
* **Database:** SQLite (Default)

---

## 🚀 Installation & Local Setup

Follow these steps to get the project running on your local machine:

### 1. Clone the Project

git clone [https://github.com/jayeshhsathawane/Pulse-Hospital-Bhandara_Website.git](https://github.com/jayeshhsathawane/Pulse-Hospital-Bhandara_Website.git)
cd Pulse-Hospital-Bhandara_Website

**Create and Activate Virtual Environment**
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

**Install Required Packages**
pip install -r requirements.txt

**Configure Environment Variables**
*Create a file named .env in the root directory (next to manage.py) and add the following:*

SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

**Apply Database Migrations**
python manage.py makemigrations
python manage.py migrate

**Create a Superuser (For Dashboard Access)**
python manage.py createsuperuser

**Run the Server**
python manage.py runserver
Access the site at: http://127.0.0.1:8000/
