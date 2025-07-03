# Smart-Resume-Screener# Smart Resume Screener

An AI-powered resume screening and job matching platform built with FastAPI, Next.js, and PostgreSQL.

## 🚀 Features

- **Resume Parsing**: Extract key information from resumes automatically
- **Smart Scoring**: AI-powered scoring based on job requirements
- **Team Collaboration**: Share reviews and notes with your team
- **Job Management**: Create and manage job postings with requirements
- **Database Migrations**: Automated database schema management with Alembic

## 🏗️ Architecture

- **Backend**: FastAPI with SQLModel (PostgreSQL)
- **Frontend**: Next.js 15 with TypeScript and Tailwind CSS
- **Database**: PostgreSQL 15
- **Containerization**: Docker & Docker Compose
- **Migrations**: Alembic

## 📋 Prerequisites

- Docker and Docker Compose
- Node.js 20+ (for local development)
- Python 3.11+ (for local development)

## 🛠️ Quick Start

### 1. Clone the repository
```bash
git clone <repository-url>
cd Smart-Resume-Screener
```

### 2. Start all services
```bash
docker-compose up --build
```

This will start:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **Database**: PostgreSQL on port 5432

### 3. Access the application
- Open your browser and go to http://localhost:3000
- The frontend will automatically check the backend connection
- API documentation is available at http://localhost:8000/docs

## 🗄️ Database Setup

The database is automatically initialized when the backend starts. The system includes:

- **Automatic table creation** via SQLModel
- **Alembic migrations** for schema versioning
- **Initial migration** with all required tables

### Manual Migration (if needed)
```bash
# Run migrations
docker-compose exec backend alembic upgrade head

# Create new migration
docker-compose exec backend alembic revision --autogenerate -m "description"

# Rollback migration
docker-compose exec backend alembic downgrade -1
```

## 🔧 Development

### Backend Development
```bash
cd apps/backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend Development
```bash
cd apps/frontend
npm install
npm run dev
```

### Database Connection
```bash
# Connect to PostgreSQL
docker-compose exec db psql -U resume_user -d resume_screener
```

## 📁 Project Structure

```
Smart-Resume-Screener/
├── apps/
│   ├── backend/
│   │   ├── app/
│   │   │   ├── api/           # API routes
│   │   │   ├── core/          # Core configuration
│   │   │   ├── models/        # Database models
│   │   │   ├── schemas/       # Pydantic schemas
│   │   │   ├── services/      # Business logic
│   │   │   ├── alembic/       # Database migrations
│   │   │   ├── db.py          # Database connection
│   │   │   ├── main.py        # FastAPI app
│   │   │   └── init_db.py     # Database initialization
│   │   ├── Dockerfile
│   │ 