# Create a downloadable README.md file for the user

readme_content = """
# Habot Employee Management API

A Django REST API built using SOLID architecture principles, JWT authentication,
pagination, filtering, and Swagger (OpenAPI) documentation.

---

## Features
- Employee CRUD APIs
- JWT Authentication
- Pagination & Filtering
- Swagger Documentation
- SOLID Architecture
- src-based Django layout

---

## Project Architecture

habot/
├── manage.py
├── src/
│   ├── config/
│   ├── apps/
│   │   └── employees/
│   │       ├── models.py
│   │       ├── serializers.py
│   │       ├── selectors.py
│   │       ├── services.py
│   │       ├── views.py
│   │       └── urls.py
│   └── common/

---

## SOLID Principles
- Single Responsibility per layer
- Business logic isolated in services
- Query logic isolated in selectors
- Easy to extend and test

---

## Setup Instructions

### Install dependencies
pip install -r requirements.txt

### Run migrations
python manage.py makemigrations
python manage.py migrate

### Create superuser
python manage.py createsuperuser

### Run server
python manage.py runserver

---

## JWT Authentication

POST /api/token/

Use the access token as:
Authorization: Bearer <ACCESS_TOKEN>

---

## Swagger Documentation

Swagger UI:
http://127.0.0.1:8000/api/docs/

Steps:
1. Open Swagger
2. Click Authorize
3. Enter Bearer <ACCESS_TOKEN>
4. Test APIs

---

## API Endpoints

POST   /api/employees/
GET    /api/employees/
GET    /api/employees/{id}/
PUT    /api/employees/{id}/
DELETE /api/employees/{id}/

---

## Author
Ravinder Atri
"""

path = "/mnt/data/README.md"
with open(path, "w", encoding="utf-8") as f:
    f.write(readme_content)

path
