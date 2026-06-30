import json
import os
import datetime

DIARY_FILE = "diary.json"

# Load diary if file exists
if os.path.exists(DIARY_FILE):
    with open(DIARY_FILE, "r") as f:
        diary = json.load(f)
else:
    diary = {}

print("⬇ My Personal Diary ⬇")
input("Press Enter if you want us to create your own personal diary:")

pin_choice = input("Do you want a pin in your diary or not (yes / no): ").lower()

# Function to save diary to JSON file
def save_diary():
    with open(DIARY_FILE, "w") as f:
        json.dump(diary, f, indent=4)

# Login with pin if chosen
if pin_choice == "yes":
    while True:
        lock = input("Enter a 4-digit pin: ")
        if len(lock) == 4 and lock.isdigit():
            print("Pin Created Successfully")
            break
        else:
            print("Invalid pin. Please enter exactly 4 digits.")

    while True:
        login = input("Enter your pin to login: ")
        if login == lock:
            print("Login Successful")
            break
        else:
            print("Wrong Pin. Try again.")

elif pin_choice == "no":
    print("Your personal Diary with no password generated Successfully")
    input("Press enter to begin:")

else:
    print("Invalid Input received! Please fill only yes or no")
    exit()

# Menu Loop
menu = '''--- Menu ---
1. Add New Entry
2. View All Entries
3. Remove an Entry
4. Exit'''

while True:
    print("\n" + menu)
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 4.")
        continue

    if choice == 1:
        input("Press Enter if you want to begin your entry:")
        content = input("Write Content Here: ")
        timestamp = datetime.datetime.now().strftime("Date-%d/%m/%Y Time-%H:%M:%S")
        diary[timestamp] = content
        save_diary()
        print("Diary Updated Successfully.")

    elif choice == 2:
        if not diary:
            print("No entries found.")
        else:
            input("Press Enter to see all entries.")
            for date, content in diary.items():
                print(f'''⭕ {date}
☑️ Content- {content}''')

    elif choice == 3:
        if not diary:
            print("No entries to remove.")
        else:
            print("Your Entries⬇")
            for date in diary:
                print(date)
            c = input("Which entry do you want to remove? Fill exact date from your entries: ")
            if c in diary:
                del diary[c]
                save_diary()
                print(f"{c} removed successfully.")
            else:
                print(f"Item {c} isn't found in your entries. Please fill a valid date shown above.")

    elif choice == 4:
        print("Exited Successfully. Thanks for using our program.")
        break

    else:
        print("Invalid choice. Please select from 1 to 4.")
