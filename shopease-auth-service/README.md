@"
# ShopEase Authentication Microservice

A standalone FastAPI Authentication Microservice for the ShopEase application.

## Features

- User registration
- Duplicate email validation
- Secure BCrypt password hashing
- JWT authentication
- JWT expiration
- Protected user profile endpoint
- JWT token verification
- Password change
- Active/inactive user validation
- MySQL 8 database
- SQLAlchemy ORM
- Alembic database migrations
- Docker and Docker Compose
- MySQL healthcheck
- Environment-based configuration
- Swagger/OpenAPI documentation

## Tech Stack

- Python 3.11+
- FastAPI
- SQLAlchemy
- MySQL 8
- Alembic
- PyMySQL
- Pydantic Settings
- python-jose
- Passlib
- BCrypt
- Docker
- Docker Compose

## Project Structure

```text
shopease-auth-service/
├── app/
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── database/
│   │   └── connection.py
│   ├── models/
│   │   └── user_model.py
│   ├── routers/
│   │   └── auth_routes.py
│   ├── schemas/
│   │   └── auth_schema.py
│   ├── services/
│   │   └── auth_service.py
│   └── main.py
├── alembic/
├── Dockerfile
├── docker-compose.yml
├── alembic.ini
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md