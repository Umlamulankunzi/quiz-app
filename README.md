# Quiz App

## Overview

The **Quiz App** is an interactive web application where users can answer multiple-choice questions. The application features scoring, time limits, and feedback. It’s built using Flask for the backend and CSS for the frontend, with SQLite used for development and MySQL for deployment.

## Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS
- **Database:** SQLite (development), MySQL (deployment)
- **Authentication:** JWT (JSON Web Tokens)

## Features

- User authentication with JWT
- Scoring and feedback on quiz answers
- Time limits for each quiz
- Responsive design for various devices
- API endpoints to manage quiz questions and results

## Setup Instructions

### Prerequisites

- Python 3.x
- Flask
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
   - For deployment with MySQL, configure the `config.py` with MySQL connection details.

6. **Run the application:**

   ```bash
   python app.py
   ```

## Usage

1. **Authentication:**

   - Users can register and log in using JWT for secure session management.

2. **Taking a Quiz:**

   - After logging in, users can access quizzes, answer questions, and receive feedback.

3. **Managing Quiz Questions:**

   - Admins can add, update, and delete quiz questions through the REST API.

## API Endpoints

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

   - Update the `config.py` file with MySQL connection details.

   Still under development. will be updated with specific details.

2. **Deploy the application:**

   - Deploy on platforms like Heroku, AWS, or any server supporting Flask applications.

## Contributing

1. **Fork the repository** and create a new branch for your changes.
2. **Make your changes** and test thoroughly.
3. **Submit a pull request** with a clear description of your changes.

## License

This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for details.