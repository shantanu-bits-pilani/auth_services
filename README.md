# Auth Service

## Description
The Auth Service handles user authentication and authorization. It provides endpoints for user registration, login, and user management.

## Dependencies
- Flask=2.1.1
- Werkzeug=2.1.1
- pymongo=4.0.1

## Endpoints
- `POST /register`: Register a new user.
- `POST /login`: Authenticate a user and return a token.
- `GET /users`: Retrieve a list of all users.

### Register
- **URL:** `/register`
- **Method:** `POST`
- **Request Body:**
  ```json
    {
        "username": "string",
        "password": "string"
    }
- **Response:**
    - 201 Created if the user is registered successfully.
    - 400 Bad Request if the user already exists.

### Login
- **URL:** `/login`
- **Method:** `POST`
- **Request Body:**
    ``` json 
    {
    "username": "string",
    "password": "string"
    }
- **Response:**
    - 200 OK if the login is successful.
    - 401 Unauthorized if the credentials are invalid.

## Environment Variables
- `MONGO_URI`: MongoDB connection string.


## Running the Service
    To run the service, use Docker Compose:

``` docker-compose up --build auth-service ```
