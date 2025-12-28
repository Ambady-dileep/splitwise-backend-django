Splitwise Backend (Django) ⚖️💰

A professional, resume-ready backend inspired by Splitwise for group expense tracking and settlements.

Key Highlights

Designed with clean architecture: service layer separates business logic from views

Implements accurate expense splitting and minimal settlement transactions

Django Admin for internal management of users, groups, and expenses

Built with Python, Django, and PostgreSQL — production-ready

Fully testable backend with unit tests for settlements and business rules

Tech Stack

Python 3.13 | Django 5.x | PostgreSQL

ORM-driven models, Decimal arithmetic for precision

No unnecessary apps — lean and maintainable structure

Project Structure (Professional Layout)
splitwise_backend/
│
├── apps/
│   ├── users/        # User management
│   ├── groups/       # Groups & memberships
│   └── expenses/     # Expenses, shares, and settlement services
│
├── config/           # Django settings, URLs, WSGI
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md

Setup (3 Steps to Run Locally)

Clone & activate venv

git clone https://github.com/Ambady-dileep/splitwise-backend-django.git
cd splitwise-backend-django
python -m venv venv
venv\Scripts\activate   # Windows


Install dependencies & configure PostgreSQL

pip install -r requirements.txt
# Create DB in PostgreSQL:
# CREATE DATABASE splitwise_db;
# Update config/settings.py with DB credentials
python manage.py migrate
python manage.py createsuperuser


Run server & test endpoints

python manage.py runserver
# Admin: http://127.0.0.1:8000/admin/