students={}

subjects=["Maths","Science","English","Hindi"]

while True:
    print("""===== 🎓 Student Result Manager =====

1. Add Student
2. View All Students
3. Show Result
4. Search Student
5. Exit""")
    try:
        choose=int(input("Enter your choice : "))
        print("----------------------------------")
        if choose==1:
            print("----------------------------------")
            
            name= input("Enter name of the student: ")
            marks_individual = []
            for l in subjects:
                marks=int(input(f"Enter Marks of {l}: "))
                if marks<0 or marks>100:
                    print("Invalid Input . Please Enter marks under 0-100")
                else:
                    marks_individual.append(marks)
                    students[name]=marks_individual.copy()
                    print("\n----------------------------------")
                    
            print("You sucessfully Added:")
            print(f"Student Name: {name}")
            for m in range(0,len(marks_individual)):
                print(f"{name} marks in {subjects[m]} :", marks_individual[m])
            print("✅ Student added successfully!\n")
            
        
        
        elif choose==2:
            print("""----------------------------------""")
            print("📋 All Students:")
            if not students:
                print("You had added 0 students")
                print("Please add minimum 1 student to check")
            else:
                for i , n in enumerate ( students.keys(),start=1):
                    print(i,n)
                    
        elif choose==3:
            if not students:
                print("Please Add Minimum 1 students To Continue")
            else:
                find = input("Enter name of student:")
                if find in students.keys():
                    print("Showing Result of ",find)
                    marks = students[find]
                    total =sum(marks)
                    per = (total/400)*100
                    
                    print(f"Name : {find}")
                    for i in range(len(subjects)):
                        print(f"Marks in {subjects[i]}: {marks[i]}")
                    print("Total:",total)
                    print(f"Percentage: {per}%")
                    
                    
                    if per >= 90:
                        grade = "A+"
                    elif per>= 75:
                        grade = "A"
                    elif per >= 60:
                        grade = "B"
                    elif per >= 50:
                        grade = "C"
                    else:
                        grade = "Fail"

                    print(f"Grade: {grade}")
                    
                    if total>=132:
                        status = "Pass"
                    else:
                        status="Fail"
                        
                    print("Status : ",status)
                else:
                    print(f"Student {find} didnt find")
        elif choose==4:
            if not students:
                print("There is no student in your data")
            else:
                se = input("Search Name of the Student :")
                if se in students.keys():
                    for o in students.keys():
                        if o==se:
                            print("🔍 Student Found!")
                            print("Name:",se)
                            print("Marks:",students[se])
                        else:
                            print(f"No , Name {se} not found")
        elif choose==5:
            save = input("Do you want to save this data in your system (yes/no):").lower()
            if save.lower()=="yes":
                filename = input("Enter name of the file :").lower()
                with open(filename+".txt","w") as file:
                    file.write("ID    NAME      MARKS  \n")
                    file.write(str(students) + "\n")
                print(f"File Saved as {filename}.txt✔️")
                print("GoodBye")
                break
            else:
                print("Goodbye")
                break
                    
                    
                
                
                
                
    except (TypeError , ValueError):
        print("Input Type Didint Matched. Please enter only integer")
        print("Please try again")