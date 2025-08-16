import datetime

expenses = []  # list to store expenses



def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/Other): ")
    date = datetime.date.today()  # current date
    expenses.append({"amount": amount, "category": category, "date": date})
    print("✅ Expense added successfully!\n")



def view_expenses():
    if not expenses:
        print("No expenses found!\n")
        return
    


    print("\nYour Expenses:")
    for exp in expenses:
        print(f"{exp['date']} - {exp['category']} - ₹{exp['amount']}")
    print()




def check_daily_limit(limit=500):
    today = datetime.date.today()
    total = sum(exp['amount'] for exp in expenses if exp['date'] == today)
    print(f"Today's total spending: ₹{total}")

    
    if total > limit:
        print("⚠️ Warning: You crossed your daily limit!\n")
    else:
        print("✅ You are within your daily limit.\n")




def main():
    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Check Daily Limit")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            check_daily_limit()
        elif choice == "4":
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice, try again!\n")

main()
