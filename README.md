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

Quiz Wiz is an online platform designed for both users and developers. Users can explore and take quizzes on a variety of subjects. Developers can utilize our comprehensive API to integrate quizzes into their own applications.

## Features

- **User Registration & Authentication**: Secure registration and login system, using django default auth.
- **Interactive Quizzes**: Users can take timed quizzes with immediate feedback upon completion.
- **Quiz Management**: users can upload their questions.
- **Leaderboard**: still under development.
- **API for Developers**: Access to our quiz repository through a RESTful API.
- **Dashboard**: still under development.
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
- Django Rest framework

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/umlamulankunzi/quiz-app.git
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

- **Api root**: `GET /api/v1/`
- **list categories**: `GET /api/v1/categories/`
- **list one category**: `GET /api/v1/categories/category<id>`
- **list category questions**: `GET /api/v1/category/questions/category/<id>/`

Refer to the [API documentation](#) for detailed information.


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

Quiz Wiz is released under the Apache  2 License. See the [LICENSE](LICENSE) file for details..


------------------------------------------------------------------------------------------------
