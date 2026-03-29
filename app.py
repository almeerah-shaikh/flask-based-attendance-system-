from flask import Flask, render_template, redirect, url_for, request, session, flash
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Dummy user for demonstration
USERS = {'admin': 'password'}

STUDENTS_FILE = 'students.txt'
ATTENDANCE_FILE = 'attendance.txt'

# Helper functions for file operations
def load_students():
    if not os.path.exists(STUDENTS_FILE):
        return []
    with open(STUDENTS_FILE, 'r') as f:
        return [line.strip() for line in f.readlines()]

def save_student(name):
    with open(STUDENTS_FILE, 'a') as f:
        f.write(name + '\n')

def load_attendance():
    if not os.path.exists(ATTENDANCE_FILE):
        return []
    with open(ATTENDANCE_FILE, 'r') as f:
        return [line.strip() for line in f.readlines()]

def save_attendance(student, status):
    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    day_str = now.strftime('%A')
    record = f"{date_str} ({day_str}) - {student}: {status}"
    with open(ATTENDANCE_FILE, 'a') as f:
        f.write(record + '\n')

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if USERS.get(username) == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    students = load_students()
    attendance = load_attendance()
    return render_template('dashboard.html', students=students, attendance=attendance)

@app.route('/add_student', methods=['POST'])
def add_student():
    if 'username' not in session:
        return redirect(url_for('login'))
    name = request.form['student_name']
    if name:
        save_student(name)
    return redirect(url_for('dashboard'))

@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    if 'username' not in session:
        return redirect(url_for('login'))
    student = request.form['student']
    status = request.form.get('status')
    if student and status:
        save_attendance(student, status)
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
