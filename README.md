Library Management System

A simple Library Management System built using Flask, SQLAlchemy, and Flask-WTF for form handling and validation. 
This project allows users to manage members and books, with CRUD (Create, Read, Update, Delete) operations for both.

Features:

Add, Edit, and Delete Members

Add, Edit, and Delete Books

Home page that lists members and books

Form validation for adding members and books

Flash messages for successful and failed operations

Technologies Used

Flask: Python web framework for building the application.

SQLAlchemy: ORM for database interactions.

Flask-WTF: Form handling library with validation.

SQLite: Database used for storing data (library.db).


Prerequisites

Before running the project, ensure you have the following installed:Python 3.x pip (Python package installer)

Install Dependencies and Clone the Repository:git clone https://github.com/your-username/library-management.git

Create a Virtual Environment (optional but recommended):source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required libraries: pip install -r requirements.txt


Running the Application
Start the Flask application: python app.py
This will start the Flask development server. By default, the app will be available at http://127.0.0.1:5000/.

Access the Home Page: Open your browser and go to http://127.0.0.1:5000/. This page will display all members and books in your library.

Add a Member: Navigate to /add_member to add a new member.

Edit a Member: Click "Edit" next to a member's name to edit their details.

Delete a Member: Click "Delete" next to a member's name to delete them.

Add a Book: Navigate to /add_book to add a new book.

Edit a Book: Click "Edit" next to a book title to edit the book details.

Delete a Book: Click "Delete" next to a book title to delete it.
