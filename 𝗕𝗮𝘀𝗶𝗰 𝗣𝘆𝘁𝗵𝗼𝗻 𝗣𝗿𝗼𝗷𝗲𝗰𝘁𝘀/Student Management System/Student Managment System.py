import json

# Try to load existing student data from file, otherwise start empty
try:
    with open("students.json", "r") as f:
        students = json.load(f)
except FileNotFoundError:
    students = {}

def add_student():
    roll = input("Enter Roll No: ")
    if roll in students:
        print("Student with this roll number already exists!")
        return
    name = input("Enter Name: ")
    marks = {}
    for subject in ["Math", "Science", "English"]:
        marks[subject] = int(input(f"Enter marks for {subject}: "))
    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully!")

def update_marks():
    roll = input("Enter Roll No: ")
    if roll in students:
        subject = input("Enter subject to update (Math/Science/English): ")
        if subject in students[roll]["marks"]:
            new_marks = int(input("Enter new marks: "))
            students[roll]["marks"][subject] = new_marks
            print("Marks updated successfully!")
        else:
            print("Subject not found!")
    else:
        print("Student not found!")

def view_report():
    roll = input("Enter Roll No: ")
    if roll in students:
        data = students[roll]
        print(f"\nReport Card for {data['name']}:")
        total = 0
        for sub, score in data["marks"].items():
            print(f"{sub}: {score}")
            total += score
        avg = total / len(data["marks"])
        print(f"Average: {avg:.2f}")
        if avg >= 90:
            grade = "A+"
        elif avg >= 75:
            grade = "A"
        elif avg >= 60:
            grade = "B"
        elif avg >= 40:
            grade = "C"
        else:
            grade = "F"
        print(f"Grade: {grade}\n")
    else:
        print("Student not found!")

def save_data():
    with open("students.json", "w") as f:
        json.dump(students, f, indent=4)

# Main menu loop
while True:
    print("\n--- Student Report Card Manager ---")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. View Report Card")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_marks()
    elif choice == "3":
        view_report()
    elif choice == "4":
        save_data()
        print("Data saved. Exiting program.")
        break
    else:
        print("Invalid choice, try again.")
