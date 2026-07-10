# IntelliFlow AI

# API Documentation

## Base URL

```
http://localhost:8000/api/v1
```

---

# Authentication

## POST /auth/register

Register a new user.

### Request

```json
{
  "full_name": "Sneha Patil",
  "email": "snehapatil0209@gmail.com",
  "password": "********"
}
```

### Response

```json
{
  "message": "User registered successfully"
}
```

---

## POST /auth/login

Authenticate user.

### Response

```json
{
  "access_token": "JWT_TOKEN",
  "token_type": "Bearer"
}
```

---

# Documents

## POST /documents/upload

Upload a company document.

---

## GET /documents

List all uploaded documents.

---

## DELETE /documents/{id}

Delete a document.

---

# AI Assistant

## POST /ai/chat

Ask questions about company documents.

---

# Tasks

## GET /tasks

Retrieve assigned tasks.

---

## POST /tasks

Create a new task.

---

# Meetings

## POST /meetings/upload

Upload meeting audio.

---

## Analytics

## GET /analytics/dashboard

Retrieve dashboard statistics.