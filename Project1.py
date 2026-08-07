#Student Placement Management System
students = []

while True:
    print("\n===== PLACEMENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete student")
    print("6. Check Placement Eligibility")
    print("7. Exit")

    choice = input("Enter your choice: ")

#If choice 1

    if choice == "1":
        print("\n--- Add Student ---")

        name = input("Enter student name: ")
        usn = input("Enter USN: ")
        branch = input("Enter branch: ")

        try:
            cgpa = float(input("Enter CGPA: "))
            backlogs = int(input("Enter number of backlogs: "))
        except ValueError:
            print("Invalid CGPA or backlog value.")
            continue

        student = {
            "name": name,
            "usn": usn,
            "branch": branch,
            "cgpa": cgpa,
            "backlogs": backlogs
        }

        students.append(student)
        print("Student added successfully!")

#if choice 2

    elif choice == "2":
        print("\n--- Student List ---")

        if len(students) == 0:
            print("No students found.")

        else:
            for student in students:
                print("\nName:", student["name"])
                print("USN:", student["usn"])
                print("Branch:", student["branch"])
                print("CGPA:", student["cgpa"])
                print("Backlogs:", student["backlogs"])

#if choice 3

    elif choice == "3":
        print("\n--- search Student ---")

        search_usn = input("Enter USN to search: ")

        found = False

        for studnent in students:
            if student["usn"].lower() == search_usn.lower():

                print("\nStudent Found!")
                print("Name:", student["name"])
                print("USN:", student["usn"])
                print("Branch:", student["branch"])
                print("CGPA:", student["cgpa"])
                print("Backlogs:", student["backlogs"])

                found = True
                break

        if found == False:
            print("Student not found.")

#if choice 4

    elif choice == "4":
        print("\n--- Update student ---")

        update_usn = input("Enter USN of student to update: ")

        found = False

        for student in students:
            if student["usn"].lower() == update_usn.lower():
                print("\nStudent found!")
                student["name"] = input("Enter new name: ")
                student["branch"] = input("Enter new branch:")

                try:
                    student["cgpa"] = float(input("Enter new CGPA: "))
                    student["backlogs"] = int(input("Enter new number of backlogs: "))

                except ValueError:
                    print("Invalid CGPA or backlog value.")
                    break

            if found == False:
                print("Student not found.")

#If choice 5

    elif choice == "5":
        print("\n--- Delete student ---")

        delete_usn = input("Enter USN of student to delete: ")
        found = False
        for student in students:
            if student["usn"].lower() == delete_usn.lower():
                students.remove(student)
                print("Student deleted successfully!")
                found = True
                break

        if found == False:
            print("Student not found.")

#if choice 6

    elif choice == 6:
        print("\n--- Placemet Eligibility ---")

        search_usn = input("Enter student USN: ")

        found = False
        for student in students:
            if student["usn"].lower() == search_usn.lower():

                found = True
                print("\nStudent:", student["name"])
                print("CGPA:", student["cgpa"])
                print("Backlogs:", student["backlogs"])

                #Palcement criteria

                if student["cgpa"] >= 7.5 and student["backlogs"] == 0:
                    print("\nResult : ELIGIBLE FOR PLACEMENT")
                else:
                    print("\nResult : NOT ELIGIBLE FOR PLACEMENT")

                    if student["cgpa"] < 7.5:
                        print("Reason: CGPA is below 7.5")
                    if student["backlogs"] > 0:
                        print("Reason: student has active backlogs")
                    break

        if found == False:
            print("student not found.")

#if choice 7


    elif choice == "7":
        print("\nThank you for using the Placement Management System.")
        print("program closed")
        break

    #invalid option

    else:
        print("\nInvalid coice.")
        print("Please enter a number from 1 to 7.")