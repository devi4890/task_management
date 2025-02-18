Task Management System
Overview
A simple backend Task Management System built using Django REST Framework (DRF) and JWT tokens for secure user authentication. The system supports CRUD (Create, Read, Update, Delete) operations to manage tasks.

Features
JWT Authentication: Secure authentication using JWT tokens for user login.
CRUD Operations:
Create: Add new tasks.
Read: Retrieve the list of tasks or specific task details.
Update: Modify existing task details.
Delete: Remove a task.
Requirements
Python 3.x
Django 3.x or higher
Django REST Framework
djangorestframework-simplejwt
SQLite (or any other database)
Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/devi4890/task_management.git
Navigate to the project folder:

bash
Copy
Edit
cd task_management_system
Create a virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Setup
Apply migrations:

bash
Copy
Edit
python manage.py migrate
Create a superuser:

bash
Copy
Edit
python manage.py createsuperuser
Run the development server:

bash
Copy
Edit
python manage.py runserver
Your server should now be running at http://127.0.0.1:8000/.

Usage
Authentication
To authenticate, use JWT tokens. Send a POST request to /api/token/ with your username and password to receive the token.

Example request:

bash
Copy
Edit
POST /api/token/
Content-Type: application/json
{
  "username": "your_username",
  "password": "your_password"
}
This will return a JWT token that you can include in the headers for authenticated requests.

API Endpoints
POST /api/tasks/: Create a new task.

GET /api/tasks/: Retrieve the list of all tasks.

GET /api/tasks/{id}/: Retrieve details of a specific task by ID.

PUT /api/tasks/{id}/: Update a specific task by ID.

DELETE /api/tasks/{id}/: Delete a specific task by ID.

Default Router Setup
DRF's default router will automatically handle the URL routing for CRUD operations.

In your urls.py file:

python
Copy
Edit
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('api/', include(router.urls)),
]
This automatically generates the necessary routes for managing tasks.

Notes
JWT Token: After logging in, include the JWT token in the Authorization header for all requests that require authentication.
Task Model: The task model contains fields such as title, description, and status (e.g., "pending", "completed").
API Usage: All endpoints require a valid JWT token to be passed in the headers of requests that involve creating, updating, or deleting tasks.
