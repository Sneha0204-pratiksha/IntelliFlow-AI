# Database Design

## Users

- id
- full_name
- email
- password
- role
- department
- created_at

---

## Documents

- id
- title
- filename
- uploaded_by
- upload_date

---

## Chats

- id
- user_id
- question
- answer
- created_at

---

## Tasks

- id
- title
- description
- assigned_to
- status
- priority
- due_date

---

## Meetings

- id
- title
- audio_file
- summary
- action_items

---

## Notifications

- id
- message
- user_id
- is_read