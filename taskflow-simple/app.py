from flask import Flask, render_template, request, redirect, session
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecret'

# Create database and tables if not exist
def init_db():
    with sqlite3.connect("tasks.db") as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE,
                        password TEXT)""")
        cur.execute("""CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT,
                        description TEXT,
                        assignee TEXT,
                        status TEXT,
                        due_date TEXT)""")

init_db()

@app.route('/')
def index():
    if 'user' not in session:
        return redirect('/login')
    con = sqlite3.connect("tasks.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    return render_template('index.html', tasks=tasks, user=session['user'])

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            with sqlite3.connect("tasks.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                con.commit()
            return redirect('/login')
        except:
            return "Username already exists!"
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pw = request.form['password']
        con = sqlite3.connect("tasks.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?", (user, pw))
        if cur.fetchone():
            session['user'] = user
            return redirect('/')
        else:
            return "Invalid login"
    return render_template('login.html')

@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form['title']
    desc = request.form['description']
    assignee = request.form['assignee']
    due_date = request.form['due_date']
    with sqlite3.connect("tasks.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO tasks (title, description, assignee, status, due_date) VALUES (?, ?, ?, ?, ?)",
                    (title, desc, assignee, "To Do", due_date))
        con.commit()
    return redirect('/')

@app.route('/update_status/<int:task_id>')
def update_status(task_id):
    with sqlite3.connect("tasks.db") as con:
        cur = con.cursor()
        cur.execute("SELECT status FROM tasks WHERE id=?", (task_id,))
        status = cur.fetchone()[0]
        next_status = {"To Do": "In Progress", "In Progress": "Completed", "Completed": "Completed"}[status]
        cur.execute("UPDATE tasks SET status=? WHERE id=?", (next_status, task_id))
        con.commit()
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)
