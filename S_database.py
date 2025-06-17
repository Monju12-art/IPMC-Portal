import sqlite3

conn = sqlite3.connect('S_database.db')
c = conn.cursor()


c.execute("DROP TABLE IF EXISTS grades")
c.execute("DROP TABLE IF EXISTS students")


# Create students table (add course if needed)
c.execute('''
    CREATE TABLE IF NOT EXISTS students (
        index_number TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        password TEXT NOT NULL,
        course TEXT NOT NULL
    )
''')

# Create grades table with index_number as foreign key
c.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        index_number TEXT NOT NULL,
        module TEXT NOT NULL,
        grade TEXT NOT NULL,
        course TEXT NOT NULL,
        FOREIGN KEY (index_number) REFERENCES students(index_number)
    )
''')


c.execute("INSERT INTO students VALUES ('IPMC1001', 'Emmanuella Owusu', 'Ema123', 'Software Engineering')")
c.execute("INSERT INTO students VALUES ('IPMC1002', 'Andrew Zubah', 'Zubah123', 'System Engineering')")
c.execute("INSERT INTO students VALUES ('IPMC1003', 'Frank Cooper', 'frank123', 'Database Management')")
c.execute("INSERT INTO students VALUES ('IPMC1004', 'Freeman Lionel', 'free123', 'Graphic Design')")

c.execute("INSERT INTO students VALUES ('IPMC1005', 'Princess Dennis', 'dennis123', 'Software Engineering')")
c.execute("INSERT INTO students VALUES ('IPMC1006', 'Andrews Vesielle', 'ves123', 'Software Engineering')")
c.execute("INSERT INTO students VALUES ('IPMC1007', 'Akim Mensah', 'akim123', 'Software Engineering')")
c.execute("INSERT INTO students VALUES ('IPMC1008', 'Blessing Copper', 'bless123', 'Software Engineering')")


# For Software Engineering student
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1001', 'Intro to SE', 'A', 'Software Engineering')")
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1001', 'Data Structures', 'B+', 'Software Engineering')")
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1001', 'Algorithms', 'A-', 'Software Engineering')")
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1001', 'Web Development', 'B', 'Software Engineering')")
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1001', 'Database Systems', 'A', 'Software Engineering')")

# new princess 
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1005', 'Intro to SE', 'B', 'Software Engineering')")


c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1005', 'Data Structures', 'A', 'Software Engineering')")

c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1005', 'Algorithms', 'C', 'Software Engineering')")

c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1005', 'Web Development', 'A', 'Software Engineering')")

c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1005', 'Database Systems', 'A', 'Software Engineering')")
# 


# new Andrews
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1006', 'Intro to SE', 'B', 'Software Engineering')")

c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1006', 'Data Structures', 'A', 'Software Engineering')")

c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1006', 'Algorithms', 'A', 'Software Engineering')")

c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1006', 'Web Development', 'A', 'Software Engineering')")

c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1006', 'Database Systems', 'C', 'Software Engineering')")
# 


# new Akim
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1007', 'Intro to SE', 'C', 'Software Engineering')")

c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1007', 'Data Structures', 'A', 'Software Engineering')")

c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1007', 'Algorithms', 'B', 'Software Engineering')")

c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1007', 'Web Development', 'A', 'Software Engineering')")

c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1007', 'Database Systems', 'C', 'Software Engineering')")
# 


# new Cooper
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1008', 'Intro to SE', 'B', 'Software Engineering')")

c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1008', 'Data Structures', 'A', 'Software Engineering')")

c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1008', 'Algorithms', 'A', 'Software Engineering')")

c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1008', 'Web Development', 'A', 'Software Engineering')")

c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1008', 'Database Systems', 'C', 'Software Engineering')")
# 




# For System Engineering student
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1002', 'System Fundamentals', 'B+', 'System Engineering')")
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1002', 'Network Basics', 'A', 'System Engineering')")
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1002', 'Operating Systems', 'A-', 'System Engineering')")
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1002', 'Security', 'B', 'System Engineering')")
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1002', 'Cloud Computing', 'A', 'System Engineering')")

# For Database Management student
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1003', 'Database Systems', 'A-', 'Database Management')")
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1003', 'SQL Basics', 'B+', 'Database Management')")
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1003', 'Data Modeling', 'A', 'Database Management')")
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1003', 'NoSQL Databases', 'B', 'Database Management')")
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1003', 'Database Security', 'A', 'Database Management')")

# For Graphic Design student
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1004', 'Graphics Design Basics', 'B', 'Graphic Design')")
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1004', 'Typography', 'A-', 'Graphic Design')")
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1004', 'Color Theory', 'A', 'Graphic Design')")
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1004', 'Digital Illustration', 'B+', 'Graphic Design')")
c.execute("INSERT INTO grades (index_number, module, grade, course) VALUES ('IPMC1004', 'Branding', 'A', 'Graphic Design')")




# ...existing code...

# Create staff table
c.execute('''
    CREATE TABLE IF NOT EXISTS staff (
        staff_id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

c.execute("DELETE FROM staff")

# Insert one staff member
c.execute("INSERT INTO staff VALUES ('STAFF100', 'Mr Josiah Tetteh', 'mr josiah tetteh', 'password123')")



conn.commit()
conn.close()