## write student data in csv

import csv

def write_student_data():
    """
    Handles writing data to students.csv.
    Gives two options:
    1. Write predefined default data.
    2. Overwrite the file with new user-input data.
    """

    print("\nWrite Options:")
    print("1. Write default student data")
    print("2. Overwrite file and enter new student data manually")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        students = [
            ["Name", "Age", "Grade"],
            ["Rahul", 16, "10th"],
            ["Sakshi", 15, "9th"],
            ["Aman", 17, "11th"]
        ]

        with open("student.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(students)

        print("✔ Default student data written successfully!\n")

    elif choice == "2":
        # User enters new data
        rows = []
        rows.append(["Name", "Age", "Grade"])  # Header

        n = int(input("How many students do you want to enter? "))

        for i in range(n):
            print(f"\nEnter details for student {i+1}:")
            name = input("Name: ")
            age = input("Age: ")
            grade = input("Grade: ")
            rows.append([name, age, grade])

        with open("student.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("✔ New data saved! Old data removed.\n")

    else:
        print("Invalid choice! Returning to main menu.\n")


def read_student_data():
    """
    Reads and prints all data from students.csv.
    """

    print("\nReading student data:\n")

    try:
        with open("student.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("File not found! Write data first.\n")


def append_student_data():
    """
    Appends a new student record to students.csv without removing old data.
    """

    print("\nEnter new student details to append:")

    name = input("Name: ")
    age = input("Age: ")
    grade = input("Grade: ")

    with open("student.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, grade])

    print("✔ New student appended successfully!\n")


def menu():
    """
    Main menu for File Handling operations on students.csv.
    User can choose: Write, Read, Append, or Exit.
    """

    while True:
        print("===== Student CSV File Menu =====")
        print("1. Write")
        print("2. Read")
        print("3. Append")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            write_student_data()
        elif choice == "2":
            read_student_data()
        elif choice == "3":
            append_student_data()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")


# Start the menu
menu()
