from expense_manager import ExpenseManager
manager = ExpenseManager()
while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1-add an expense")
    print("2-remove an expense")
    print("3-show all the expenses")
    print("4-Calculate the total amount of expenses")
    print("5-filtrate expenses by category")
    print("6-Calculate monthly expenses")
    print("7-Show spending totals by category")
    print("9-Exit")
    try:
      choice = int(input("Choose an option: "))
    except ValueError:
      print("Please enter a number.")
      continue
    if choice == 9:
        print("Goodby!")
        break
    elif choice == 1:
        manager.add_expense()
    elif choice == 2:
        manager.remove()
    elif choice == 3:
        manager.get_all_expenses()
    elif choice == 4:
        print("the total of your expense are: ",manager.calculate_total())
    elif choice == 5:
        category = input("Would type a category for your expenses")
        manager.get_expenses_by_category(category)
    elif choice == 6:
        try:
            month = int(input("Enter the month (1-12): "))
            year = int(input("Enter the year (e.g. 2026): "))
            if month < 1 or month > 12:
                print("Invalid month")
            else:
                total = manager.calculate_monthly_total(month, year)
                print(f"Total expenses for {month}/{year}: {total}")
        except ValueError:
            print("Please enter valid integers.")
    elif choice == 7:
      totals = manager.calculate_category_totals()
      if not totals:
         print("No expenses found")
      else:
         for category, total in totals.items():
            print(category, ":", total)
    
    elif choice == 8:
      expenses = manager.sort_expenses_by_amount()
      if not expenses:
         print("No expenses found")
      else:
         for expense in expenses:
            print(expense.id, expense.category,
                  expense.amount, expense.date)
    else:
        print("Invalid choice. Please try again.")

