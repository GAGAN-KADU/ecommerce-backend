# E-Commerce Backend with Flask

## Overview

This project implements a simple e-commerce backend using Flask, featuring user authentication, product management, shopping cart functionality, and order checkout (mock). The backend follows Object-Oriented Programming (OOP) principles and uses JWT (JSON Web Token) for user authentication and authorization.

### Key Features

- **User Authentication**: Register and login functionality with JWT-based token authentication.
- **Product Management**: Add, update, delete, and view product details.
- **Shopping Cart**: Add and remove products from the cart.
- **Order Checkout**: Mock checkout process.
- **Authorization**: Secure API routes using JWT authentication.

## Key Design Principles

### 1. **Object-Oriented Programming (OOP)**:
- **Classes**: Used to define entities like `User`, `Product`, `Cart`, and `Order` in `models.py`, each with relevant attributes and methods to handle their operations.
- **Services**: Business logic is encapsulated in service functions or methods, improving code modularity and maintainability.

### 2. **Abstraction**:
- **Database Operations**: SQLAlchemy models abstract raw SQL queries, making database interactions easier and cleaner.
- **Business Logic**: Logic for user authentication, product management, and order processing is abstracted into service methods, simplifying the rest of the code.

### 3. **Decorators**:
- **JWT Authentication**: The `@jwt_required()` decorator secures routes that need authentication by checking for a valid JWT token.
- **Custom Decorators**: Used to enforce access control, such as `admin_required`, for restricted routes.

### 4. **Exception Handling**:
- **Flask Error Handling**: Custom error handlers return meaningful messages for errors like 404 or 500.
- **Custom Exceptions**: Specific errors (e.g., `ProductNotFoundException`) are caught and handled gracefully, ensuring the app doesn't crash.

---

## Project Structure
ecommerce-backend/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── auth.py
│   ├── cart.py
│   └── checkout.py
│
├── config.py
├── run.py
└── requirements.txt


## Requirements

Make sure you have Python 3.x installed. You can create a virtual environment to manage your project dependencies.

To set up the environment:

### 1. Clone the Repository

```bash
git clone https://github.com/GAGAN-KADU/ecommerce-backend.git
cd ecommerce-backend
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the Required Libraries

```bash
pip3 install -r requirements.txt
```

### DB Configuration

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

```bash
python3 init_db.py
```

### 4. Run the Application

```bash
python3 app.py
```

The application will be available at http://localhost:5005.

## API Endpoints

The API endpoints are as follows:

### Authentication

- **POST /register**: Register a new user.
- **POST /login**: Login an existing user.

### Products

- **GET /products**: Get all products.

### Cart

- **GET /cart**: Get the user's cart.
- **POST /cart**: Remove a product to the cart.

### Checkout

- **POST /process: Checkout the cart.


### Steps for Usage:

1. **Set up the project**: Clone the repository and follow the instructions in the **Requirements** section to install dependencies and set up the database.
2. **Run the app**: Use `python app.py` to start the app.
3. **Test the endpoints**: Use Postman or cURL to make requests to the endpoints, passing JWT tokens for protected routes.
