print("Welcome to Expense Tracker" )
all_expenses = []
while True:
    print("\n========= MENU ===========")
    print("\n1. Add Expense\n2. View All Expenses\n3. View Total Expenses\n4. Exit\n========================== ")
    user_choice = int(input("\nEnter your choice(1-4): "))
    #Add Expence
    if user_choice == 1:
        print("Add Your Expences")    
        print("=================")
        expense = {}
        fields = ["Date", "Category", "Description", "Amount"]
        for item in fields:
            expense[item] = input(f"Enter your {item} : ") 

        all_expenses.append(expense)
        print("\nExpense saved successfully!")
    #Show expense
    elif user_choice == 2:
        print("\n=== Expense Details ===")

        if not all_expenses:
            print("\nNo expenses recorded yet.")
        else:
            for count, item in enumerate(all_expenses, 1):
                print(f"Expense {count}:")
                for key, value in item.items():
                    print(f"{key:<12}: {value}")
                print("-" * 25)
    #Sum all the expenses
    elif user_choice == 3:
        print("\n=== Total Expenses ===")
        total = 0

        for item in all_expenses:
            total += float(item["Amount"])

        print(f"Your total expenses amount: {total}")
    #Exit
    elif user_choice == 4:
        print("\nClosing Tracker. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please pick a number from 1 to 4.")
