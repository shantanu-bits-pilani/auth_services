# Auth Service

## Description
The Auth Service handles user authentication and authorization.

## Endpoints

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

## Running the Service
    To run the service, use Docker Compose:

``` docker-compose up --build auth-service ```
