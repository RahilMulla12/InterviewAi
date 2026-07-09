# Interview AI Backend

A Django REST Framework backend for the Interview AI Platform. It provides secure authentication, resume parsing, AI-powered interview question generation, answer evaluation, analytics, and user profile management.

## Features

* JWT Authentication
* User Registration & Login
* Resume Upload (PDF)
* Resume Skill Extraction using Groq AI
* AI Interview Question Generation
* Answer Evaluation & Scoring
* Interview Analytics
* User Profile Management
* PostgreSQL Database
* REST API using Django REST Framework

---

## Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL
* JWT Authentication
* Groq API
* PyMuPDF
* Gunicorn
* WhiteNoise
* Render

---

## Project Structure

```text
Backend/
│── accounts/
│── analytics/
│── dashboard/
│── interviews/
│── resumes/
│── Backend/
│── media/
│── manage.py
│── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Backend
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_secret_key

DEBUG=True

DATABASE_URL=postgresql://username:password@localhost:5432/interview_db

GROQ_API_KEY=your_groq_api_key
```

---

## Database Migration

```bash
python manage.py makemigrations

python manage.py migrate
```

Create an admin user:

```bash
python manage.py createsuperuser
```

---

## Run Development Server

```bash
python manage.py runserver
```

Backend will be available at:

```
http://127.0.0.1:8000/
```

---

## API Endpoints

### Authentication

| Method | Endpoint              |
| ------ | --------------------- |
| POST   | `/api/users/`         |
| POST   | `/api/token/`         |
| POST   | `/api/token/refresh/` |

### Resume

| Method | Endpoint        |
| ------ | --------------- |
| GET    | `/api/resumes/` |
| POST   | `/api/resumes/` |

### Interviews

| Method | Endpoint                                   |
| ------ | ------------------------------------------ |
| GET    | `/api/interviews/`                         |
| POST   | `/api/interviews/`                         |
| POST   | `/api/interviews/{id}/generate_questions/` |

### Questions

| Method | Endpoint                             |
| ------ | ------------------------------------ |
| GET    | `/api/interviews/{id}/questions/`    |
| POST   | `/api/questions/{id}/submit_answer/` |

### Analytics

| Method | Endpoint          |
| ------ | ----------------- |
| GET    | `/api/analytics/` |

### Dashboard

| Method | Endpoint          |
| ------ | ----------------- |
| GET    | `/api/dashboard/` |

### Profile

| Method | Endpoint         |
| ------ | ---------------- |
| GET    | `/api/users/me/` |
| PATCH  | `/api/users/me/` |

---

## Deployment

Backend is deployed on Render.

Production stack:

* Django
* Gunicorn
* WhiteNoise
* PostgreSQL
* Render

---

## Author

**Rahil Mulla**
