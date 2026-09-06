from prettytable import PrettyTable

menu = """========================================
💼 PERSONAL FINANCE TRACKER
========================================

1. Add Expense
2. View All Expenses
3. View Summary
4. Edit/Delete Expense
5. Set Monthly Budget
6. Exit"""

expenses = []

food=[]
travel = []
shopping =[]

categories = """1. Food
2. Travel
3. Shopping"""

while True:
    print(menu)
    choose=int(input("Enter your choice:"))
    print("----------------------------------------")
    if choose==1:
        print("➕ ADD NEW EXPENSE\n")
        amount = int(input("Enter amount:"))
        print(categories)
        category=int(input("Enter category (Food/Travel/Shopping):"))
        if category==1:
            cat ="Food"
            food.append(amount)
        elif category==2:
            cat = "Travel"
            travel.append(amount)
        elif category==3:
            cat = "Shopping"
        
            shopping.append(amount)
        date=input("Enter date (DD-MM-YYYY):")
        des=input("Enter description:")
        
        expenses.append({
        "amount": amount,
        "category": cat,
        "date": date,
        "desc": des
        })
        print("✅ Expense added successfully!")
        
    elif choose == 2:
        
        table = PrettyTable(["ID","Amount","Category","Date","Description"])

        for i, exp in enumerate(expenses, start=1):
            table.add_row([
                i,
                exp["amount"],
                exp["category"],
                exp["date"],
                exp["desc"]
            ])

        print(table)
    elif choose==3:
        print("-----Summary-----")
        print("Total spend on Food: ₹", sum(food))
        print("Total spend on Shopping: ₹", sum(shopping))
        print("Total spend on Travel: ₹", sum(travel))
        
    elif choose == 4:
        
        print("-----Edit / Delete Expenses ---------")
        if not expenses:
            print("⚠️ No expenses to edit/delete!")
            continue


        table = PrettyTable(["ID","Amount","Category","Date","Description"])
        for i, exp in enumerate(expenses, start=1):
            table.add_row([i, exp["amount"], exp["category"], exp["date"], exp["desc"]])
        print(table)

        try:
            idx = int(input("Enter Expense ID: ")) - 1

            if idx < 0 or idx >= len(expenses):
                print(" Invalid ID Pleease Enter Again")
                continue

            action = input("Type 'edit' or 'delete': ").lower()

            if action == "delete":
                removed = expenses.pop(idx)

                # also remove from category list
                if removed["category"] == "Food":
                    food.remove(removed["amount"])
                elif removed["category"] == "Travel":
                    travel.remove(removed["amount"])
                elif removed["category"] == "Shopping":
                    shopping.remove(removed["amount"])

                print("Expense deleted successfully!")

            elif action == "edit":
                new_amount = int(input("Enter new amount: "))
                new_date = input("Enter new date: ")
                new_desc = input("Enter new description: ")

                old = expenses[idx]
                if old["category"] == "Food":
                    food.remove(old["amount"])
                    food.append(new_amount)
                elif old["category"] == "Travel":
                    travel.remove(old["amount"])
                    travel.append(new_amount)
                elif old["category"] == "Shopping":
                    shopping.remove(old["amount"])
                    shopping.append(new_amount)

                expenses[idx]["amount"] = new_amount
                expenses[idx]["date"] = new_date
                expenses[idx]["desc"] = new_desc

                print(" Expense updated!")

            else:
                print(" Invalid action")

        except ValueError:
            print(" Please enter valid input")
    elif choose==5:
        print("------ Set Montly Budget ---------")
        bud = int(input("Enter your monthly Budget:"))
        
        total = sum(food)+sum(shopping) + sum(travel)
        print(f"Montly Budget Set : {bud}")
        budget = bud-total
        print("Budget Left :",budget)
    elif choose==6:
        exit()
