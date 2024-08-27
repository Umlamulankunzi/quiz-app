# Quiz Wiz

Welcome to **Quiz Wiz**, an interactive quiz application where users can test their knowledge on various topics through engaging quizzes. The platform is designed for quiz enthusiasts, educators, and developers who want to leverage our vast repository of quizzes through an API.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Custom Authentication](#custom-authentication)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Project Description

Quiz Wiz is an online platform designed for both users and developers. Users can explore and take quizzes on a variety of subjects, track their progress, and compete on leaderboards. Developers can utilize our comprehensive API to integrate quizzes into their own applications. The platform features user roles such as Admins, Quiz Masters, and Developers, each with specific permissions.

## Features

- **User Registration & Authentication**: Secure registration and login system with customizable user roles.
- **Interactive Quizzes**: Users can take timed quizzes with immediate feedback upon completion.
- **Quiz Management**: Admins and Quiz Masters can create, update, and delete quizzes.
- **Leaderboard**: Track top performers across different quizzes.
- **API for Developers**: Access to our quiz repository through a RESTful API.
- **Dashboard**: Personalized dashboards for users and quiz masters to track their activities.
- **Mobile-Friendly**: Fully responsive design optimized for mobile devices.

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Database**: SQLite (Development), MySQL (Production)
- **Authentication**: Django's built-in authentication system with custom roles (`is_quiz_master`, `is_developer`) and Django Rest Framework Basic Authentication and Session management for the API.
- **Deployment**: Options include Railway or PythonAnywhere
- **Version Control**: Git

## Installation

### Prerequisites

- Python 3.x
- Django 3.x
- Bootstarp 5.x
- MySQL (for production)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/umlamulankunzi/quiz-app.gi
   cd quiz-app
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   - For development, SQLite is configured by default.
   - For production, configure MySQL in `settings.py`.

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   Open your web browser and go to `http://localhost:8000/`.

## Usage

### User Roles

- **Admin**: Can manage all users and quizzes.
- **Quiz Master**: Can create, update, and manage their own quizzes. Requires Admin approval for publication.
- **Regular User**: Can take quizzes and view leaderboards.
- **Developer**: Can access the quiz API.

### Frontend

- **Homepage**: Introduction to the platform and a call to action.
- **Quizzes**: Browse and take quizzes on various subjects.
- **Dashboards**: Personalized dashboards for users and quiz masters.
- **About**: Information about the website and website developers.
- **Contact**: Provides a platform to contact website admins.
- **Api-info**: Get information on the REST API.

### Developer API

- **Endpoint**: `/api/v1/`
- **Authentication**: Developers and Admins can access the API with custom authentication.
- **Documentation**: Comprehensive API docs are available [here](#).

## API Documentation

Developers can interact with Quiz Wiz's API to access quiz data, create new quizzes, and more. The API requires authentication based on the `is_developer` or `is_admin` user roles.

### Available Endpoints

- **List Quizzes**: `GET /api/quizzes/`
- **Quiz Detail**: `GET /api/quizzes/<id>/`
- **Create Quiz**: `POST /api/quizzes/`
- **Update Quiz**: `PATCH /api/quizzes/<id>/`
- **Delete Quiz**: `DELETE /api/quizzes/<id>/`

Refer to the [API documentation](#) for detailed information.

## Custom Authentication

The API access is restricted to users with the `is_developer` or `is_admin` roles. A custom permission class, `IsDeveloperOrAdmin`, is implemented to ensure secure access to API endpoints.

## Deployment

### Production

For deployment,I plan to deploy on platforms like Railway or PythonAnywhere, I plan to follow these steps:

1. **Configure production settings**:
   - Set `DEBUG = False` in `settings.py`.
   - Configure allowed hosts and database settings for MySQL.

2. **Deploy the application**:
   - Use Git to push to your hosting service.
   - Set up environment variables as needed.

3. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Collect static files**:
   ```bash
   python manage.py collectstatic
   ```

5. **Run the application**.


## License

Quiz Wiz is released under the Apache License. See the [LICENSE](LICENSE) file for details..


------------------------------------------------------------------------------------------------

# Quiz App

## Overview

The **Quiz App** is an interactive web application where users can answer multiple-choice questions. The application features scoring, time limits, and feedback. It’s now built using Django for the backend and CSS for the frontend, with SQLite used for development and MySQL for deployment.

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS
- **Database:** SQLite (development), MySQL (deployment)
- **Authentication:** Django's built-in authentication system

## Features

- User authentication with Django's built-in authentication system
- Scoring and feedback on quiz answers
- Time limits for each quiz
- Responsive design for various devices
- API endpoints to manage quiz questions and results (bonus feature)

## Setup Instructions

### Prerequisites

- Python 3.x
- Django
- SQLite (for development)
- MySQL (for deployment)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/umlamulankunzi/quiz-app.git
   cd quiz-app
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set up the database:**

   - For development with SQLite, the database will be initialized automatically.
   - For deployment with MySQL, configure the `settings.py` with MySQL connection details.

6. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

7. **Run the application:**

   ```bash
   python manage.py runserver
   ```

## Usage

1. **Authentication:**

   - Users can register and log in using Django's built-in authentication system.

2. **Taking a Quiz:**

   - After logging in, users can access quizzes, answer questions, and receive feedback.

3. **Managing Quiz Questions:**

   - Admins can add, update, and delete quiz questions through the Django admin panel or REST API (if implemented).

## API Endpoints (Bonus Feature)

- **GET /api/quizzes**: Retrieve a list of available quizzes.
- **GET /api/quizzes/{id}**: Retrieve a specific quiz by ID.
- **POST /api/quizzes**: Add a new quiz (admin only).
- **PUT /api/quizzes/{id}**: Update an existing quiz (admin only).
- **DELETE /api/quizzes/{id}**: Delete a quiz (admin only).
- **POST /api/answers**: Submit answers for a quiz.
- **GET /api/users/{id}/results**: Retrieve quiz results for a user.

## Testing

Still under development.

## Deployment

1. **Configure MySQL:**

   - Update the `settings.py` file with MySQL connection details.

   Still under development. Will be updated with specific details.

2. **Deploy the application:**

   - Deploy on platforms like Heroku, AWS, or any server supporting Django applications.

## Contributing

1. **Fork the repository** and create a new branch for your changes.
2. **Make your changes** and test thoroughly.
3. **Submit a pull request** with a clear description of your changes.

## License

This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for details.