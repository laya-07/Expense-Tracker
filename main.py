from datetime import datetime
expenses=[]
def add_expense():
    try:
        amount=int(input("Enter the Amount:"))
    except ValueError:
        print("Please enter numbers only!")
        return
    category=input("Enter the category:")
    date=datetime.now().strftime("%d-%m-%Y")
    expense = f"{date},{amount},{category}\n"
    expenses.append(expense)
    file=open("expenses.txt","a")
    file.write(expense)
    file.close()
    print("\nExpense Saved Successfully!\n")
def view_expenses():
    print("\n===== All Expenses =====\n")
    file=open("expenses.txt","r")
    data=file.readlines()
    total=0
    for index,line in enumerate(data,start=1):
        date,amount,category=line.strip().split(",")
        print(f"{index}.Date: {date} | Category: {category} | Amount: ₹{amount}")
        total+=int(amount)
    file.close()
    print("\n==========================")
    print(f"Total Expense: ₹{total}\n")
def delete_expense():
    file=open("expenses.txt","r")
    data=file.readlines()
    file.close()
    print("\n==== Expenses ====")
    for index,line in enumerate(data,start=1):
        date,amount,category=line.strip().split(",")
        print(f"{index}. {date} | {amount} | {category}")
    delete_number=int(input("Enter Expense number to delete:"))
    if 1<=delete_number<=len(data):
        data.pop(delete_number-1)
        file=open("expenses.txt","w")
        file.writelines(data)
        file.close()
        print("\nExpense Deleted Successfully!\n")
    else:
        print("\nInvalid Expense Number\n")
def search_expense():
    search_category=input("Enter category to search:").lower()
    try:
        file=open("expenses.txt", "r")
    except FileNotFoundError:
        print("\nNo expenses found.\n")
        return
    data=file.readlines()
    file.close()
    found=False
    print("\n===== Search Results =====\n")
    for line in data:
        date,amount,category=line.strip().split(",")
        if category.lower()==search_category:
            print(f"Date: {date} | Amount: ₹{amount} | Category: {category}")
            found=True
    if not found:
        print("No expenses found.")
def category_report():
    file=open("expenses.txt","r")
    data=file.readlines()
    file.close() 
    category_totals={}
    for line in data:
        date,amount,category=line.strip().split(",")
        amount=int(amount)
        if category in category_totals:
            category_totals[category]+=amount
        else:
            category_totals[category]=amount
    print("\n===== Category -wise Report =====\n")
    for category, total in category_totals.items():
        print(f"{category} | ₹{total}")
while True:

    print("==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Search Expense")
    print("5.Category Report")
    print("6.Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        search_expense()
    elif choice == "5":
        category_report()
    elif choice == "6":
        print("Exiting program....")
        break

    else:
        print("Invalid Choice\n")
