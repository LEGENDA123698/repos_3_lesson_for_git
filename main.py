import sqlite3

connect = sqlite3.connect("univer.db")
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    major TEXT
)  
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS  courses(
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT,
    instructor TEXT
)  
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS  student_courses(
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(course_id) REFERENCES courses(id)
)  
''')


while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Вийти")

    choice = input("Оберіть опцію (1-7): ")

    # Додавання нового студента
    if choice == "1":
        name = input("name: ")
        age = int(input("age: "))
        major = input("major: ")
        cursor.execute('''
            INSERT INTO students (name, age, major)
            VALUES (?, ?, ?)''', (name, age, major))
        connect.commit()

    # Додавання нового курсу
    elif choice == "2":
        course_name = input("course name please: ")
        instructor = input("instructor name please: ")
        cursor.execute('''
            INSERT INTO courses (course_name, instructor)
            VALUES (?, ?)''', (course_name, instructor))
        connect.commit()

    # Показати список студентів
    elif choice == "3":
        cursor.execute('''SELECT * FROM students''')
        students = cursor.fetchall()
        for student in students:
            print(student)

    # Показати список курсів
    elif choice == "4":
        cursor.execute('''SELECT * FROM courses''')
        courses = cursor.fetchall()
        for course in courses:
            print(course)

    # Зареєструвати студента на курс
    elif choice == "5":
        student_id = int(input("student_ID: "))
        course_id = int(input("course_ID: "))
        cursor.execute('''
            INSERT INTO student_courses (student_id, course_id)
            VALUES (?, ?)''', (student_id, course_id))
        connect.commit()

    # Показати студентів на конкретному курсі
    elif choice == "6":
        cursor.execute('''SELECT students.name, courses.course_name
                        FROM courses
                        INNER JOIN student_courses ON student_courses.course_id = courses.course_id
                        INNER JOIN students ON students.student_id = student_courses.student_id''')
        res = cursor.fetchall()

        print(res)

       
    elif choice == "7":
        break

    else:
        print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")

