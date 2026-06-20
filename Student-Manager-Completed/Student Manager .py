students = []

while True:

    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        name = input("Enter student name: ")
        roll = input("Enter roll number: ")

        student = {
            "name": name,
            "roll": roll
        }

        students.append(student)

    elif choice == "2":

        for student in students:

            print("Name:", student["name"])
            print("Roll:", student["roll"])

    elif choice == "3":

        break

    else:

        print("Invalid choice")