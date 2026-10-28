# Healthcare Backend API

A healthcare backend built with Django, Django REST Framework, PostgreSQL, and JWT authentication.

## Features

* User registration and login
* JWT-based authentication
* Patient CRUD operations
* Doctor CRUD operations
* Patient-doctor assignments
* Input validation and access permissions
* PostgreSQL database integration

## Installation

Install dependencies:

```
pip install -r requirements.txt
```

Create a `.env` file using `.env.example` as a template and configure your PostgreSQL credentials.

Create the database:

```
CREATE DATABASE healthcare_db;
```

Apply migrations:

```
python manage.py makemigrations
python manage.py migrate
```

Start the server:

```
python manage.py runserver
```

## API Endpoints

| Method                  | Endpoint            | Description                |
| ----------------------- | ------------------- | -------------------------- |
| POST                    | /api/auth/register/ | Register                   |
| POST                    | /api/auth/login/    | Login                      |
| GET, POST               | /api/patients/      | List or create patients    |
| GET, PUT, PATCH, DELETE | /api/patients/{id}/ | Manage a patient           |
| GET, POST               | /api/doctors/       | List or create doctors     |
| GET, PUT, PATCH, DELETE | /api/doctors/{id}/  | Manage a doctor            |
| GET, POST               | /api/mappings/      | List or create assignments |
| DELETE                  | /api/mappings/{id}/ | Delete an assignment       |

Authenticated endpoints require:

```
Authorization: Bearer <access_token>
```

