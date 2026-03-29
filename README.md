# Almeerah Student Attendance System Web App (Flask)

This is a Flask-based web application for managing student attendance, named after Almeerah. It features user authentication, student management, and attendance tracking, all through a simple web interface. Data is stored in plain text files for easy setup and portability.

## Features
- User login/logout
- Add and list students
- Mark and view attendance
- Simple HTML interface
- File-based data storage (no database required)

## How to Run
1. Install dependencies:
   ```
   pip install flask
   ```
2. Start the app:
   ```
   python app.py
   ```
3. Open your browser and go to `http://127.0.0.1:5000`

## Project Structure
```
app.py
students.txt
attendance.txt
templates/
    login.html
    dashboard.html
static/
README.md
```

## Default Login
- Username: admin
- Password: password

You can change these in `app.py`.
