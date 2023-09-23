#!/usr/bin/env python3

from app import db
from models import Task
from app import app  # Import the Flask app instance

# Create and add some initial tasks to the database
if __name__ == '__main__':
    with app.app_context():  # Create an app context to work with the app and database
        db.create_all()

        task1 = Task(title='Buy groceries', description='Milk, eggs, bread')
        task2 = Task(title='Finish project', description='Complete project by Friday')
        task3 = Task(title='Go for a run', description='Run 5 kilometers')

        db.session.add(task1)
        db.session.add(task2)
        db.session.add(task3)

        db.session.commit()


