# Scalable Task Management System

A full-stack Task Management System built using Django REST Framework, PostgreSQL, JWT Authentication, Role-Based Authorization, and Vanilla JavaScript.

The application allows users to register, log in securely, access protected resources, and perform complete CRUD operations on tasks through both REST APIs and a simple frontend dashboard.

---

## Features

### Authentication & Authorization

* User Registration
* User Login
* JWT Authentication using SimpleJWT
* Protected API Endpoints
* Role-Based Authorization
* Admin-only role management endpoint

### Task Management

* Create Tasks
* View Tasks
* Update Tasks
* Delete Tasks
* User-specific task access control

### Frontend Integration

* Login Page
* Registration Page
* Protected Dashboard
* Task Creation
* Task Listing
* Task Updating
* Task Deletion
* API Success/Error Handling

### API Documentation

* Swagger UI Documentation
* OpenAPI Schema Generation

### Database

* PostgreSQL Integration
* Relational Database Design
* Optimized Model Relationships

---

## Technology Stack

### Backend

* Python 3.12
* Django
* Django REST Framework
* SimpleJWT
* drf-spectacular

### Database

* PostgreSQL

### Frontend

* HTML5
* Bootstrap 5
* Vanilla JavaScript

### Version Control

* Git
* GitHub

---

## Project Structure

```text
PrimetradeAi_assignment/
│
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   └── urls.py
│
├── tasks/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── templates/
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
├── static/
│   └── js/
│       ├── login.js
│       ├── register.js
│       └── dashboard.js
│
├── assignment/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py
```

---

## Database Schema

### User

| Field    | Type            |
| -------- | --------------- |
| id       | Integer         |
| username | CharField       |
| email    | EmailField      |
| password | Hashed Password |
| is_admin | Boolean         |

### Task

| Field       | Type             |
| ----------- | ---------------- |
| id          | Integer          |
| title       | CharField        |
| description | TextField        |
| created_by  | ForeignKey(User) |
| created_at  | DateTimeField    |
| updated_at  | DateTimeField    |

### Relationship

```text
User (1) ---------> (Many) Tasks
```

Each user can create multiple tasks.

---

## API Endpoints

### Authentication

#### Register User

```http
POST /api/accounts/register/
```

#### Login User

```http
POST /api/accounts/login/
```

Returns:

```json
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}
```

---

### Role Management

#### Make User Admin

```http
PATCH /api/accounts/make-admin/<user_id>/
```

Admin Only Endpoint.

---

### Task APIs

#### Create Task

```http
POST /api/tasks/fetch_or_create/
```

#### Fetch Tasks

```http
GET /api/tasks/fetch_or_create/
```

#### Update Task

```http
PATCH /api/tasks/fetch_create_update/<id>/
```

#### Delete Task

```http
DELETE /api/tasks/fetch_create_update/<id>/
```

---

## JWT Authentication

Protected endpoints require:

```http
Authorization: Bearer <access_token>
```

Example:

```http
Authorization: Bearer eyJhbGciOiJIUzI1Ni...
```

---

## API Documentation

Swagger UI:

```text
/api/docs/
```

OpenAPI Schema:

```text
/api/schema/
```

---

## Installation & Setup

### Clone Repository

```bash
git clone <repository-url>
cd PrimetradeAI_assignment
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Virtual Environment

Mac/Linux

```bash
source env/bin/activate
```

Windows

```bash
env\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your-secret-key

DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```
### Configure PostgreSQL

Create a PostgreSQL database and update:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "your_db_name",
        "USER": "your_username",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run Development Server

```bash
python manage.py runserver
```

Application:

```text
http://127.0.0.1:8000/
```

---

## Security Considerations

* Passwords are securely hashed using Django's authentication system.
* JWT-based authentication for protected resources.
* Role-based authorization for administrative operations.
* Input validation using DRF serializers.
* User-specific task ownership enforcement.
* Unauthorized requests return proper HTTP status codes.

---

## Scalability & Deployment Readiness

The application is designed with scalability in mind.

### Current Design

* Modular Django application architecture.
* Stateless JWT authentication.
* PostgreSQL relational database.
* RESTful API design.
* Separation of frontend and backend concerns.

### Future Improvements

* Redis caching for frequently accessed data.
* Celery for background job processing.
* Docker containerization.
* Nginx reverse proxy.
* Load balancing across multiple application instances.
* CI/CD pipelines.
* Cloud deployment on AWS, Azure, or GCP.
* Migration toward microservice architecture if application scale increases.

---

## Evaluation Criteria Coverage

### API Design

* REST Principles
* Proper HTTP Status Codes
* Modular Architecture
* Swagger Documentation

### Database

* PostgreSQL Integration
* Relational Schema Design
* User-Task Relationships

### Security

* JWT Authentication
* Password Hashing
* Authorization Controls
* Serializer Validation

### Frontend

* Functional UI
* Authentication Flow
* CRUD Operations
* Error Handling

---

## Author

Sagar Singh

Backend Developer 
