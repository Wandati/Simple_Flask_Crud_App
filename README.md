# Simple Flask CRUD To-Do List App

This is a simple CRUD (Create, Read, Update, Delete) application built with Flask, a lightweight web framework in Python. It allows you to manage your to-do list with basic operations.

## Features

- **Create:** Add new tasks to your to-do list.
- **Read:** View your tasks and their details.
- **Update:** Edit the task details.
- **Delete:** Remove tasks from your to-do list.

## Prerequisites

- Python 3.6 or higher
- Flask (`pip install Flask`)
- Flask-SQLAlchemy (`pip install Flask-SQLAlchemy`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/flask-todo-app.git
   cd flask-todo-app
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:

   ```bash
   flask run
   ```

The app will be accessible at `http://localhost:8000` in your browser.

## Usage

- **Adding a Task:** Click on the "Add Task" button and fill out the form to add a new task to your to-do list.

- **Viewing Tasks:** All tasks are displayed on the homepage with options to edit or delete each task.

- **Editing a Task:** Click on the "Edit" button next to a task to modify its details.

- **Deleting a Task:** Click on the "Delete" button next to a task to remove it from your to-do list.

## Project Structure

- **app.py:** Contains the Flask application and routes.
- **models.py:** Defines the database models (e.g., Task).
- **templates/:** Contains HTML templates for rendering pages.
- **static/:** Contains static files like CSS stylesheets or client-side JavaScript.

## Contributing

Feel free to contribute to this project! You can open issues, submit pull requests, or suggest new features or improvements.

Happy task management! 😊
