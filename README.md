# Flask JWT Authentication and Protected Routes Example

This repository provides a Flask application with JWT-based authentication, user registration, login, profile
management, token refresh, protected routes, file upload, form validation, CSRF protection, and API routes exempted from
CSRF protection.

## Features

- User registration and login using JWT tokens.
- User profile management.
- Token refresh mechanism.
- Protected routes with authentication and authorization.
- File upload functionality.
- Form validation with CSRF protection.
- Exempted API routes from CSRF protection.

## Prerequisites

- Python (3.x recommended)
- Flask
- Flask-JWT-Extended
- Flask-WTF
- Flask-Uploads (for file upload handling)
- Other required packages (see `requirements.txt`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kumarnabin/flask_user_role.git
   cd flask-jwt-auth-example


2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Configure the app settings in config.py.
5. Run the application:
   ```bash
   flask run

## Usage

- Register a new user and login to obtain a JWT token.
- Access protected routes using the obtained token.
- Upload files through the provided endpoint.
- Visit profile and perform other authorized actions.

## Endpoints

- POST /auth/register: User registration.
- POST /auth/login: User login to obtain a JWT token.
- POST /auth/refresh: Refresh an expired token.
- GET /auth/profile: Get user profile information.
- POST /file/upload: Upload a file.
- POST /api/file/upload: Upload a file in an API route without CSRF protection.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Flask: https://flask.palletsprojects.com/
- Flask-JWT-Extended: https://flask-jwt-extended.readthedocs.io/
- Flask-WTF: https://flask-wtf.readthedocs.io/
- Flask-Uploads: https://pythonhosted.org/Flask-Uploads/

```bash

Feel free to copy and paste this template into your GitHub README.md file and modify it as needed for your specific application.
