import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")

conn.commit()

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    # Add Student
    if choice == "1":

        name = input("Enter name: ").strip()

        if not name:
            print("Name cannot be empty!")
            continue

        try:
            age = int(input("Enter age: "))
        except ValueError:
            print("Age must be a number!")
            continue

        cursor.execute(
            "INSERT INTO students(name, age) VALUES (?, ?)",
            (name, age)
        )

        conn.commit()
        print("Student added successfully!")

    # Show Students
    elif choice == "2":

        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()

        if not rows:
            print("No students found.")
        else:
            print("\nID\tName\tAge")
            print("-" * 25)

            for row in rows:
                print(f"{row[0]}\t{row[1]}\t{row[2]}")

    # Search Student
    elif choice == "3":

        search_name = input("Enter student name: ")

        cursor.execute(
            "SELECT * FROM students WHERE name = ?",
            (search_name,)
        )

        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(row)
        else:
            print("Student not found!")

    # Delete Student
    elif choice == "4":

        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid ID!")
            continue

        cursor.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )

        conn.commit()

        if cursor.rowcount > 0:
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    # Exit
    elif choice == "5":

        print("Exiting program...")
        break

    else:
        print("Invalid choice!")

# Close connection
conn.close()