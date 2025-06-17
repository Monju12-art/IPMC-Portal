from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for sessions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')



@app.route('/sey')
def sey():
    return render_template('sey10.html')

@app.route('/se')
def se():
    return render_template('s.e.batch8-10am.html')

@app.route('/graphic')
def graphic_design():
    return render_template('graphic.html')

@app.route('/database-management')
def database_management():
    return render_template('database_management.html')

@app.route('/register')
def register():
    return render_template('register.html')

# for dashboard
@app.route('/dashboard')
def dashboard():
    if 'student_id' not in session:
        return redirect('/login/student')
    student_name = session['name']
    print(f"DEBUG student_name: '{student_name}'")
    student_index = session['student_id']
    conn = sqlite3.connect('S_database.db')
    c = conn.cursor()
    c.execute("SELECT course FROM students WHERE index_number = ?", (student_index,))
    result = c.fetchone()
    conn.close()
    student_course = result[0] if result else None

    # Map student names to image filenames
    student_images = {
        "emmanuella owusu": "ella.jpg",
        "andrew zubah": "Zubah.jpg",
        "frank cooper": "Frank.jpg",
        "freeman lionel": "Freeman.jpg"
    }
    profile_pic = student_images.get(student_name.lower().strip(), "default.jpg")

    return render_template(
        'student_dashboard.html',
        student_name=student_name,
        student_index=student_index,
        student_course=student_course,
        profile_pic=profile_pic
    )


# Student login GET and POST
@app.route('/login/student', methods=['GET', 'POST'])
def loginstu():
    error = None
    if request.method == 'POST':
        index_number = request.form['indexNumber']
        password = request.form['password']

        conn = sqlite3.connect('S_database.db')
        c = conn.cursor()
        c.execute("SELECT name, password FROM students WHERE index_number = ?", (index_number,))
        result = c.fetchone()
        conn.close()

        if result and result[1] == password:
            session['student_id'] = index_number
            session['name'] = result[0]
            return redirect('/dashboard')
        else:
            error = 'Invalid login details'
    
    return render_template('loginstu.html', error=error)
# Staff login GET and POST
@app.route('/login/staff', methods=['GET', 'POST'])
def loginstaff():
    error = None
    if request.method == 'POST':
        staff_id = request.form.get('staffId')
        password = request.form.get('password')

        conn = sqlite3.connect('S_database.db')  # Use your main DB
        c = conn.cursor()
        c.execute("SELECT name, password FROM staff WHERE staff_id = ?", (staff_id,))
        result = c.fetchone()
        conn.close()

        if result and result[1] == password:
            session['staff_id'] = staff_id
            session['name'] = result[0]
            session['role'] = 'staff' 
            # ✅ This line lets you restrict access to staff-only pages
            
            return redirect('/staff/dashboard')
        else:
            error = 'Invalid login details'
    
    return render_template('loginstaff.html', error=error)


# staff dashboard
@app.route('/staff/dashboard')
def staff_dashboard():
    if 'staff_id' not in session:
        return redirect('/login/staff')
    conn = sqlite3.connect('S_database.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM students")
    num_students = c.fetchone()[0]
    c.execute("SELECT COUNT(DISTINCT course) FROM students")
    num_courses = c.fetchone()[0]
    conn.close()
    return render_template(
        'staff_dashboard.html',
        name=session['name'],
        num_students=num_students,
        num_courses=num_courses
    )






# Logout route for both staff and students
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login/student')


@app.route('/grades/software')
def grades_software():
    if 'student_id' not in session:
        return redirect('/login/student')
    index_number = session['student_id']
    conn = sqlite3.connect('S_database.db')
    c = conn.cursor()
    c.execute("SELECT module, grade, course FROM grades WHERE index_number = ?", (index_number,))
    grades = c.fetchall()
    conn.close()
    return render_template('grades.html', grades=grades)


@app.route('/grades/system')
def grades_system():
    if 'student_id' not in session:
        return redirect('/login/student')
    index_number = session['student_id']
    conn = sqlite3.connect('S_database.db')
    c = conn.cursor()
    c.execute("SELECT module, grade, course FROM grades WHERE index_number = ?", (index_number,))
    grades = c.fetchall()
    conn.close()
    return render_template('grades.html', grades=grades)

@app.route('/grades/database')
def grades_database():
    if 'student_id' not in session:
        return redirect('/login/student')
    index_number = session['student_id']
    conn = sqlite3.connect('S_database.db')
    c = conn.cursor()
    c.execute("SELECT module, grade, course FROM grades WHERE index_number = ?", (index_number,))
    grades = c.fetchall()
    conn.close()
    return render_template('grades.html', grades=grades)

@app.route('/grades/graphic')
def grades_graphic():
    if 'student_id' not in session:
        return redirect('/login/student')
    index_number = session['student_id']
    conn = sqlite3.connect('S_database.db')
    c = conn.cursor()
    c.execute("SELECT module, grade, course FROM grades WHERE index_number = ?", (index_number,))
    grades = c.fetchall()
    conn.close()
    return render_template('grades.html', grades=grades)


# for modules and library
@app.route('/modules/software')
def modules_software():
    return render_template('s.e. batch8-10am.html')

@app.route('/modules/system')
def modules_system():
    return render_template('sey10.html')

@app.route('/modules/database')
def modules_database():
    return render_template('database8.html')

@app.route('/modules/graphic')
def modules_graphic():
    return render_template('graphic.html')

@app.route('/library/software')
def library_software():
    return render_template('library.html', course='software_engineering')

@app.route('/library/system')
def library_system():
    return render_template('library.html', course='system_engineering')

@app.route('/library/database')
def library_database():
    return render_template('library.html', course='database')

@app.route('/library/graphic')
def library_graphic():
    return render_template('library.html', course='graphic_design')


# exams timetable
from datetime import datetime, timedelta

@app.route('/exams-timetable')
def exams_timetable():
    # Example exam schedule (replace with your real data)
    exams = [
        {"Course":"SWE", "BATCH TIME": "8-10AM","module": "Python Programming","DATE": "2025-07-10", "TIME": "9:00AM", "REQUIRED BALANCED": "NILL", "INVIGILATOR": "Sir Josiah"},
        {"Course":"GWD", "BATCH TIME": "10-12PM","module": "HTML5","DATE": "2025-07-10", "TIME": "10:00AM", "REQUIRED BALANCED": "NILL", "INVIGILATOR": "Sir Hollesi"},
         {"Course":"SYE", "BATCH TIME": "12-3PM","module": "A+","DATE": "2025-07-10", "TIME": "1:00PM", "REQUIRED BALANCED": "GHc 732", "INVIGILATOR": "Sir Prince"},
          {"Course":"DBM", "BATCH TIME": "1-3PM","module": "MySQL","DATE": "2025-07-10", "TIME": "2:00PM", "REQUIRED BALANCED": "GHc 200", "INVIGILATOR": "Madam Perpetual"},
    ]

    # Calculate resit dates: the Friday of the week after each exam
    for exam in exams:
        exam_date = datetime.strptime(exam["DATE"], "%Y-%m-%d")
        # Find the next week's Friday
        days_until_next_friday = (11 - exam_date.weekday()) % 7  # 4 is Friday
        resit_date = exam_date + timedelta(days=7 + days_until_next_friday)
        exam["resit"] = resit_date.strftime("%Y-%m-%d")

    return render_template('exams_timetable.html', exams=exams)



# 
@app.route('/staff/courses')
def manage_courses():
    # Fetch courses from your database
    conn = sqlite3.connect('S_database.db')
    c = conn.cursor()
    c.execute("SELECT code, name FROM courses")
    courses = [{'code': row[0], 'name': row[1]} for row in c.fetchall()]
    conn.close()
    return render_template('manage_courses.html', courses=courses)


# manage courses
@app.route('/staff/manage-students')
def manage_students():
    # Fetch students from your database
    conn = sqlite3.connect('S_database.db')
    c = conn.cursor()
    c.execute("SELECT index_number, name, course FROM students")
    students = [{'id': row[0], 'name': row[1], 'course': row[2]} for row in c.fetchall()]
    conn.close()
    return render_template('manage_students.html', students=students)


@app.route('/staff/edit-student/<student_id>')
def edit_student(student_id):
    # Add your edit logic here
    return f"Edit student {student_id}"

@app.route('/staff/delete-student/<student_id>')
def delete_student(student_id):
    # Add your delete logic here
    return f"Delete student {student_id}"




@app.route('/staff/software-results')
def software_results():
    conn = sqlite3.connect('S_database.db')
    c = conn.cursor()
    # Get all modules for Software Engineering
    c.execute("SELECT DISTINCT module FROM grades WHERE course = ?", ('Software Engineering',))
    modules = [row[0] for row in c.fetchall()]
    # Get all students in Software Engineering
    c.execute("SELECT index_number, name FROM students WHERE course = ?", ('Software Engineering',))
    students = c.fetchall()
    # Build results per module
    module_results = []
    for module in modules:
        c.execute("""
            SELECT s.index_number, s.name, g.grade
            FROM students s
            LEFT JOIN grades g ON s.index_number = g.index_number AND g.module = ? AND g.course = ?
            WHERE s.course = ?
        """, (module, 'Software Engineering', 'Software Engineering'))
        grades = c.fetchall()
        module_results.append({'module': module, 'grades': grades})
    conn.close()
    return render_template('software_results.html', module_results=module_results)


@app.route('/staff/profile')
def staff_profile():
    staff = {
        'name': 'Sir Josiah',
        'staff_id': 'STAFF001',
        'email': 'josiah@gmail.com',
        'role': 'Lecturer',
        'profile_pic': 'Meshack.jpg'  # or another image filename
    }
    return render_template('staff_profile.html', staff=staff)


@app.route('/library')
def library():
    if 'staff_id' in session and session.get('role') == 'staff':
        course = 'all'  # special flag to show all books
    elif 'student_id' in session:
        course = session.get('course')
    else:
        return redirect('/login/student')

    return render_template('library.html', course=course)



# submit_projects
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/submit-project', methods=['GET', 'POST'])
def submit_project():
    if 'student_id' not in session:
        return redirect('/login/student')

    message = None

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        course = request.form['course']
        file = request.files['file']

        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            # ✅ Ensure the folder exists before saving
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            file.save(filepath)

            # Save project info to database (optional)
            conn = sqlite3.connect('S_database.db')
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT,
                title TEXT,
                description TEXT,
                course TEXT,
                filename TEXT
            )''')
            c.execute("INSERT INTO projects (student_id, title, description, course, filename) VALUES (?, ?, ?, ?, ?)",
                      (session['student_id'], title, description, course, filename))
            conn.commit()
            conn.close()

            message = "Project submitted successfully!"

    return render_template('submit_project.html', message=message)


if __name__ == "__main__":
    app.run(debug=True)
