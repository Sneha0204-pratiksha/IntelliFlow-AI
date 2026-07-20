# IntelliFlow AI

Enterprise Intelligence & Workflow Automation Platform powered by AI.

## Overview

IntelliFlow AI is an AI-powered resume analysis platform that allows users to upload resumes, extract structured information using Large Language Models (Google Gemini), and securely store analysis history.

The project follows enterprise software architecture using FastAPI, SQLAlchemy, PostgreSQL, Repository Pattern, and Service Layer.

---

## Features

- User Registration
- JWT Authentication
- Role-based Authorization
- Resume Upload (PDF & DOCX)
- AI-powered Resume Parsing
- Google Gemini Integration
- Resume Analysis History
- PostgreSQL Database
- Swagger API Documentation
- Repository Pattern
- Service Layer Architecture
- Secure File Management

---

## Tech Stack

### Backend

- Python 3.12
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Alembic

### AI

- Google Gemini API
- Prompt Engineering

### Authentication

- JWT
- OAuth2 Password Flow
- Passlib (bcrypt)

### Document Processing

- PyMuPDF
- python-docx

---

## Architecture

```
Client
   │
   ▼
FastAPI API
   │
   ▼
Service Layer
   │
   ▼
Repository Layer
   │
   ▼
PostgreSQL

          │
          ▼

 Gemini AI Provider
          │
          ▼

 Resume Parser
```

---

## Project Structure

```
backend/
│
├── app/
│   ├── api/
│   ├── ai/
│   │   ├── extractors/
│   │   ├── parsers/
│   │   ├── prompts/
│   │   ├── providers/
│   │   └── services/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   └── services/
│
├── uploads/
├── requirements.txt
└── main.py
```

---

## API Modules

### Authentication

- Register User
- Login
- JWT Authentication

### Documents

- Upload Document
- Download Document
- Delete Document
- List Documents

### AI

- Analyze Resume

### Analysis

- Analyze Uploaded Document
- Get Analysis History
- Delete Analysis

### Workflows

- CRUD Operations

---

## AI Workflow

```
Upload Resume

      │

      ▼

Extract Text

      │

      ▼

Gemini AI

      │

      ▼

Structured Resume

      │

      ▼

Save Analysis

      │

      ▼

Return JSON Response
```

---

## Sample Response

```json
{
  "name": "Sneha Patil",
  "email": "example@gmail.com",
  "skills": [
    "Python",
    "FastAPI",
    "SQL"
  ]
}
```

---

## Future Enhancements

- Resume Score
- ATS Compatibility Score
- Job Description Matching
- AI Recommendations
- Dashboard
- Email Notifications
- Docker Deployment
- React Frontend

---

## Author

Sneha Patil

B.Tech Computer Science & Engineering (AI & ML)

---

## License

MIT License