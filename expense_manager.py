from storage import save_expenses, load_expenses
from models import Expense
from datetime import date
class ExpenseManager:
    def __init__(self):
       self.expenses = load_expenses()
       if self.expenses:
          self.id = max(expense.id for expense in self.expenses) + 1
       else:
            self.id = 1
    def add_expense(self):
        category = input("Try to define a category for the expense ")
        try:
           amount = float(input("would you type the amount of money "))
        except ValueError:
           print("invalid amount, type a number")
           return
        e1 = Expense(self.id, category, amount, date.today())
        self.expenses.append(e1)
        self.id += 1
        save_expenses(self.expenses)
    def remove(self):
        try:
          rid = int(input("Type the id of the expense that you want to remove "))
        except ValueError:
            print("invalid,would type an integer")
            return
        for expense in self.expenses:
            if expense.id == rid:
               self.expenses.remove(expense)
               print("Expense removed successfully")
               save_expenses(self.expenses)
               return
        print("Id not found")
    def get_all_expenses(self):
        if not self.expenses:
         print("No expenses found")
         return
        print("Your expenses are:\n")
        for expense in self.expenses:
            print(expense.id, expense.category, expense.amount, expense.date)
    def calculate_total(self):
       total = 0
       for expense in self.expenses:
          total += expense.amount
       return total
    def get_expenses_by_category(self, category):
        for expense in self.expenses:
           if expense.category.lower() == category.lower():
              print(expense.id, expense.category, expense.amount, expense.date)
    def calculate_monthly_total(self, month, year):
         total =0
         for expense in self.expenses:
            if expense.date.year == year and expense.date.month == month:
               total += expense.amount
         return total      
    def calculate_category_totals(self):
       totals = {}
       for expense in self.expenses:
          if expense.category in totals:
             totals[expense.category] += expense.amount
          else:
             totals[expense.category] = expense.amount
       return totals
     
    def sort_expenses_by_amount(self):
        return sorted(
        self.expenses,
        key=lambda expense: expense.amount,
        reverse=True
    )
  




           