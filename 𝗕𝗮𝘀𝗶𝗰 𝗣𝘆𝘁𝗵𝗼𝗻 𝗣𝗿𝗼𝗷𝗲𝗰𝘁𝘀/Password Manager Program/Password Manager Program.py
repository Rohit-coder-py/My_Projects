import random
import string
 
passwords={}
print("-----------------")
menu = """===== PASSWORD MANAGER MENU =====
1. Add Password
2. View All Passwords
3. Delete all password
4. Geneate a new password
5. Exit"""
with open("passwords.txt","a") as file:
    file.write("")
while True:
    print(menu)
    try:
        choose=int(input("Enter your choice:"))
        if choose==1:
            web = input("Enter Website Name:")
            password=input("Enter Password :")
            print("-----------------")
            
            print(f"Website: {web}")
            print(f"Password: {password}")
            print("Saved Successfully")
            passwords[web]=password
            with open("passwords.txt","a") as file:
                file.write(f"{web} : {password}\n")
        elif choose==2:
            print("-----------------")
            print("Viewing all passwords......")
            print("-----------------")

            with open ("passwords.txt","r") as f:
                c = f.read()
                print(c)
            print("-----------------")
        elif choose==3:
            print("This process can't be undone")
            confirm = input("Are you sure you want to delete all saved passwords (yes/no)").lower()
            if confirm=="yes":
                print("Deleting all saved passwords...............")
                print("After deleting you need to restart the program..")
                with open("passwords.txt","w") as ki:
                    ki.write("")
                    break
            elif confirm=="no":
                print("0 password deleted")
            else:
                print("Please enter yes or no")
        elif choose==4:
            a = [1,2,3,4,5,6,7,8,9,10]
            a9 = "abcdefghijklmnopqrstuvwxyz"
            b = list(a9)
            
            for i in a:
                c1 = random.choice(a)
                d1 = random.choice(a)
                m1 = random.choice(a)
                x1=random.choice(a)
                
            print(f"New Passoword Generated :{c1}{d1}{m1}{x1}")
        elif choose==5:
            print("Goodbye!")
            exit()
            
        else:
            print("Please Choose Any Valid Options")
    except (ValueError,TypeError):
        print("Please Enter Valid Values")
