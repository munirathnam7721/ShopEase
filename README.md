# ShopEase Product Management Microservice

A standalone Product Management Microservice developed using FastAPI and Python.

## Project Overview

ShopEase Product Management Microservice provides REST APIs for managing e-commerce products.

The service supports:

- Product creation
- Product retrieval
- Product retrieval by ID
- Product updating
- Product deletion
- Category filtering
- Pagination
- Input validation
- Error handling
- Swagger/OpenAPI documentation
- Docker containerization

Product data is stored using an in-memory Python dictionary.

## Technology Stack

- Python 3.11+
- FastAPI
- Pydantic
- Uvicorn
- python-dotenv
- Docker
- Swagger / OpenAPI
- Git / GitHub

## Project Structure

```text
shopease-product-service/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   └── product_routes.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── product_schema.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── product_model.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── product_service.py
│   │
│   └── config/
│       ├── __init__.py
│       └── settings.py
│
├── Dockerfile
├── .dockerignore
├── .env
├── requirements.txt
└── README.md