# Task Manager – Backend

This is the **backend** for the Task Manager application, built with **Django** and **Django REST Framework**.  
It provides REST APIs for managing tasks and uses **PostgreSQL (Render Managed Database)**.  
The backend is **Dockerized** and deployed on **Render**.

---

## 🚀 Tech Stack

- **Python 3**
- **Django**
- **Django REST Framework**
- **PostgreSQL (Render)**
- **Docker**
- **psycopg2**
- **django-cors-headers**

---

## 📁 Project Structure

```text
task-manager-backend/
├── backend/
│   ├── backend/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   │
│   ├── tasks/
│   │   ├── api/
│   │   │   ├── serializers.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── domain/
│   │   ├── infrastructure/
│   │   ├── services/
│   │   ├── models.py
│   │   ├── admin.py
│   │   └── migrations/
│   │
│   ├── manage.py
│   │
│   └── staticfiles/
│
├── Dockerfile
├── render.yaml
├── requirements.txt
├── .env
└── README.md
->>  Local Development Setup
1️ Create virtual environment
bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows

2️. Install dependencies
bash
pip install -r requirements.txt

3️. Configure environment variables
Create a .env file in the root directory:

env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://postgres:password@localhost:5432/task_manager

4️. Run migrations
bash
python manage.py makemigrations
python manage.py migrate

5️. Run development server
bash
python manage.py runserver
Backend will be available at:

arduino
http://localhost:8000
->>> API Base URL
bash
http://localhost:8000/api

☁️ Deployment on Render (with PostgreSQL)
1. Push code to GitHub
bash
Copy code
git add .
git commit -m "Deploy backend to Render"
git push origin main
2️. Create PostgreSQL on Render
Go to https://render.com

Click New → PostgreSQL

Create database

Copy the Internal Database URL

Example:

pgsql
Copy code
postgresql://user:password@host:5432/database
3️.Create a Web Service on Render
Click New → Web Service

Connect GitHub repository

Select task-manager-backend

Environment: Docker

4️. Set Environment Variables in Render
In Render → Environment Variables, add:

env
Copy code
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=your-render-postgres-url
Example:

env
Copy code
DATABASE_URL=postgresql://user:password@host:5432/database
5️. Build & Start Commands (Render)
Render automatically uses:

bash
Copy code
pip install -r requirements.txt
python manage.py migrate
gunicorn backend.wsgi:application
(Defined via Dockerfile or render.yaml)

6️. Enable CORS for Frontend
In settings.py:

python
Copy code
INSTALLED_APPS += ["corsheaders"]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    ...
]

CORS_ALLOWED_ORIGINS = [
    "https://task-manager-frontend.vercel.app"
]
🔗 Live Backend URL
After deployment, Render provides a URL like:

arduino
https://task-manager-backend.onrender.com
API Base URL:

arduino
https://task-manager-backend.onrender.com/api
