# ==============================
# Student Management System
# Day 6 Python Practice
# ==============================

students = []

while True:
    print("\n" + "=" * 40)
    print("      STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Average Marks")
    print("7. Show Highest Marks")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    # ----------------------------
    # Add Student
    # ----------------------------
    if choice == "1":
        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")

        english = float(input("English Marks: "))
        math = float(input("Math Marks: "))
        science = float(input("Science Marks: "))

        total = english + math + science
        average = total / 3

        if average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "Fail"

        student = {
            "Name": name,
            "Roll": roll,
            "English": english,
            "Math": math,
            "Science": science,
            "Total": total,
            "Average": average,
            "Grade": grade
        }

        students.append(student)
        print("\nStudent Added Successfully!")

    # ----------------------------
    # View Students
    # ----------------------------
    elif choice == "2":

        if len(students) == 0:
            print("\nNo student found.")

        else:
            print("\nStudent Records")
            print("-" * 70)

            for student in students:
                print("Name      :", student["Name"])
                print("Roll No   :", student["Roll"])
                print("English   :", student["English"])
                print("Math      :", student["Math"])
                print("Science   :", student["Science"])
                print("Total     :", student["Total"])
                print("Average   :", round(student["Average"], 2))
                print("Grade     :", student["Grade"])
                print("-" * 70)

    # ----------------------------
    # Search Student
    # ----------------------------
    elif choice == "3":

        roll = input("Enter Roll Number: ")

        found = False

        for student in students:
            if student["Roll"] == roll:
                found = True
                print("\nStudent Found")
                print(student)

        if not found:
            print("Student Not Found.")

    # ----------------------------
    # Update Student
    # ----------------------------
    elif choice == "4":

        roll = input("Enter Roll Number: ")

        found = False

        for student in students:

            if student["Roll"] == roll:

                found = True

                print("\nEnter New Marks")

                student["English"] = float(input("English: "))
                student["Math"] = float(input("Math: "))
                student["Science"] = float(input("Science: "))

                student["Total"] = (
                    student["English"]
                    + student["Math"]
                    + student["Science"]
                )

                student["Average"] = student["Total"] / 3

                if student["Average"] >= 80:
                    student["Grade"] = "A"
                elif student["Average"] >= 70:
                    student["Grade"] = "B"
                elif student["Average"] >= 60:
                    student["Grade"] = "C"
                elif student["Average"] >= 50:
                    student["Grade"] = "D"
                else:
                    student["Grade"] = "Fail"

                print("\nStudent Updated Successfully!")

        if not found:
            print("Student Not Found.")

    # ----------------------------
    # Delete Student
    # ----------------------------
    elif choice == "5":

        roll = input("Enter Roll Number: ")

        found = False

        for student in students:
            if student["Roll"] == roll:
                students.remove(student)
                found = True
                print("Student Deleted Successfully!")
                break

        if not found:
            print("Student Not Found.")

    # ----------------------------
    # Average of All Students
    # ----------------------------
    elif choice == "6":

        if len(students) == 0:
            print("No Data Available.")

        else:
            total_average = 0

            for student in students:
                total_average += student["Average"]

            class_average = total_average / len(students)

            print("Class Average =", round(class_average, 2))

    # ----------------------------
    # Highest Marks
    # ----------------------------
    elif choice == "7":

        if len(students) == 0:
            print("No Data Available.")

        else:

            topper = students[0]

            for student in students:

                if student["Total"] > topper["Total"]:
                    topper = student

            print("\nTopper Details")
            print("Name :", topper["Name"])
            print("Roll :", topper["Roll"])
            print("Total:", topper["Total"])
            print("Grade:", topper["Grade"])

    # ----------------------------
    # Exit
    # ----------------------------
    elif choice == "8":
        print("\nThank You!")
        print("Program Ended Successfully.")
        break

    else:
        print("\nInvalid Choice! Please Try Again.")
