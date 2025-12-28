# Splitwise Backend (Django)

A backend system inspired by Splitwise for tracking shared expenses and settling balances between group members.

## Features
- Group-based expense tracking
- Accurate expense splitting using Decimal arithmetic
- Settlement calculation with minimal transactions
- Clean service-layer architecture
- Django Admin for internal management

## Tech Stack
- Python
- Django
- PostgreSQL
- Django Admin

## Architecture
- Domain-based app structure
- Business logic isolated in services
- ORM-driven calculations

## Setup
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
