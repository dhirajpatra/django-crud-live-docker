# Django CRUD Live Application

This is a Django application that demonstrates basic CRUD operations using Django Rest Framework (DRF). The application includes payment processing with mocked and faked test cases and is set up using Docker Compose.

## Features

- Django project setup
- Django Rest Framework (DRF) integration
- CRUD operations for Payment model
- Mocked and faked test cases for credit card processing
- Docker and Docker Compose for containerized development and deployment

## Installation

### Prerequisites

- Docker
- Docker Compose

### Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/django-crud-live-app.git
    cd django-crud-live-app
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Build and start the containers:**
    ```sh
    docker-compose up --build
    ```

4. **Run migrations:**
    ```sh
    docker-compose run web python manage.py makemigrations appname
    docker-compose run web python manage.py migrate
    ```

5. **Create a superuser:**
    ```sh
    docker-compose run web python manage.py createsuperuser
    ```

### Access the Application

1. Navigate to `http://127.0.0.1:8000/` to access the application.
2. Navigate to `http://127.0.0.1:8000/admin/` to access the admin panel.

## Usage

### Access the Admin Panel

1. Navigate to `http://127.0.0.1:8000/admin/`
2. Log in using the superuser credentials created earlier.

### API Endpoints

The application provides the following API endpoints for managing payments:

- List all payments: `GET /api/payments/`
- Retrieve a single payment: `GET /api/payments/{id}/`
- Create a new payment: `POST /api/payments/`
- Update an existing payment: `PUT /api/payments/{id}/`
- Delete a payment: `DELETE /api/payments/{id}/`

### Example JSON Payload for Creating/Updating a Payment

```json
{
    "card_number": "4111111111111111",
    "card_holder": "John Doe",
    "expiration_date": "12/25",
    "amount": "100.00",
    "status": "Pending"
}
