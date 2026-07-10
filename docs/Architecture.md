# IntelliFlow AI

# System Architecture

## Architecture Style

Client-Server Architecture with AI Services

```
+--------------------------------------------------+
|                  React Frontend                  |
|--------------------------------------------------|
| Login | Dashboard | AI Chat | Documents | Tasks |
+-------------------------|------------------------+
                          |
                     REST API (HTTPS)
                          |
+--------------------------------------------------+
|                FastAPI Backend                   |
|--------------------------------------------------|
| Authentication                                  |
| User Management                                 |
| Document Service                                |
| AI Service                                      |
| Task Service                                    |
| Analytics Service                               |
+-----------|---------------|----------------------+
            |               |
     PostgreSQL        ChromaDB
            |               |
            +-------+-------+
                    |
              Gemini API
```

## Components

### Frontend
- React
- TypeScript
- Tailwind CSS

### Backend
- FastAPI
- JWT Authentication
- REST APIs

### Database
- PostgreSQL

### AI
- LangChain
- ChromaDB
- Gemini API

### Deployment
- Docker
- GitHub
- Render
- Vercel