# Advanced Calculator with History and saved file 

print(" Welcome To Smart Calculator")

history = []  

def add(a1,b1):
    c1 = a1+b1
    return c1

def subs(a2,b2):
    c2 = a2-b2
    return c2

def multi(a3,b3):
    c3 = a3*b3
    return c3

def divide(a4,b4):
    c4 = a4/b4
    return c4

def module(a5,b5):
    c5 = a5%b5
    return c5


while True:
    print("\nChoose From Below:\n")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus (Remainder)")
    print("6. View History")
    print("7. Save History to File")
    print("8. Exit")
    
    try:
        print("-----------------------")

        choose=int(input("Enter your choice:"))

        
        if choose==1:
            a1 = int(input(" Enter 1st number: "))
            b1 = int(input("Enter 2nd number :"))
            result = add(a1,b1)
            print(f"Addition of   {a1}  and {b1} is : {result}")
            tp = f" {a1} +  {b1} = {result}"
            history.append(tp)
            print("-----------------------")



        elif choose==2:
            print("-----------------------")
            a2 = int(input(" Enter 1st number:"))
            b2 = int(input("Enter 2nd  number:"))
            result = subs(a2, b2)
            print(f" Substraction of  {a2} and  {b2} is :{result}")
            tp = f"  {a2} - {b2} = {result}"
            history.append(tp)
            print("-----------------------")

 
        elif choose==3:
            print("-----------------------")
            a3 = int(input("Enter 1st number:"))
            b3 = int(input("Enter 2nd number:"))
            result = multi(a3,b3)
            print(f"Multiplication of {a3} and {b3} is :{result}")
            tp = f"{a3} * {b3}=  {result}"
            history.append(tp)
            print("-----------------------")


   
        elif choose==4:
            print("-----------------------")

            a4 = int(input("Enter 1st number:"))
            b4 = int(input("Enter 2nd number:"))
            if b4 == 0:
                print("❌ Cannot divide by zero")
                history.append(f"{a4}/{b4}=Error (division by zero)")
            else:
                result = divide(a4,b4)
                print(f"Division of {a4} and {b4} is :{result}")
                tp = f"{a4}/{b4}={result}"
                history.append(tp)
            print("-----------------------")


        
        elif choose==5:
            print("-----------------------")

            a5 = int(input("Enter 1st number:"))
            b5 = int(input("Enter 2nd number:"))
            if b5 == 0:
                print("❌ Cannot mod by zero")
                history.append(f"{a5}%{b5}=Error (cant get remainder by zero)")
            else:
                result = module(a5,b5)
                print(f"Remainder of {a5} and {b5} is :{result}")
                tp = f"{a5}%{b5}={result}"
                history.append(tp)
        


        
        elif choose==6:
            print("-----------------------")

            print("\n History:")
            if len(history)==0:
                print("No history yet")
            else:
                for i in history:
                    print(i)
            print("-----------------------")


        
        elif choose==7:
            print("-----------------------")

            filename=input("Enter filename:")
            with open(filename+".txt","w") as f:
                for i in history:
                    f.write(i + "\n")
            print(" History saved to file ✔️")
            print(f"File Saved as : {filename}.txt")
            print("-----------------------")


        
        elif choose==8:
            print("Exiting Calculator...")
            print("-----------------------")

            break

        else:
            print(" Invalid choice. pLEASE ENTER FROM 1 TO 8")

    except (ValueError,TypeError):
        print(" Please enter valid numbers only from options")