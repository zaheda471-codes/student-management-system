import json
import os

FILE_NAME=os.path.join(
    os.path.dirname(__file__),"students.json"
)

def load_students():
    try:
        with open(FILE_NAME,"r") as file:
            return json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        return[]

def save_students():
    with open(FILE_NAME,"w") as file:
        json.dump(students, file,indent=4)

students=load_students()


def add_student():
    roll=input("Enter Roll Number:")

    for student in students:
        if student["roll"]==roll:
            print("Roll Number already exits!")
            return
    name=input("Enter Student Name:")
    if not name.strip():
        print("Name cannot be empty!")
        return
    try:
        marks=float(input("Enter marks:"))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100!")
            return

    except ValueError:
        print("Please enter valid numerical marks!")
        return    

    student = {
        "roll": roll,
        "name": name,
        "marks": marks
    }

    students.append(student)
    save_students()
    print("Student added successsfully!")

def view_students():
    if not students:
        print("No student records found!")
    else:
        print("\n===== Student Records ======")

        for student in students:
            print("\nRoll Number:",student["roll"])
            print("Name:",student["name"])
            print("Marks:",student["marks"])

def search_student():
    roll=input("Enter Roll Number to search:")
    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found!")
            print("Roll Number:",student["roll"])
            print("Name:",student["name"])
            print("Marks:",student["marks"])
            return
        print("Student not found!")

def update_student():
    roll=input("Enter Roll Number to update:")
    for student in students:
        if student["roll"] == roll:
            print("Student Found!")

            new_name=input("Enter New Name:")
            new_marks=float(input("Enter New Marks:"))

            student["name"]=new_name
            student["marks"]=new_marks

            save_students()

            print("Student record updated successfully!")
            return
        print("Student not found!")

def delete_student():
    roll=input("Enter Roll Number to delete:")
    for student in students:
        if student["roll"]==roll:
            students.remove(student)
            save_students()
            print("Student record deleted successfully!")
            return
        print("Student not found!")

while True:
    print("\n======= STUDENT MANAGEMENT SYSTEM =======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice=input("Enter your choice:")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank you for for using the system")
        break
    else:
        print("Inalid choice!Try again")