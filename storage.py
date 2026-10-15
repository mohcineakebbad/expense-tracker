from models import Expense
import json
from datetime import date

def save_expenses(expenses):
    data = []

    for expense in expenses:
        data.append({
            "id": expense.id,
            "category": expense.category,
            "amount": expense.amount,
            "date": expense.date.isoformat()
        })

    with open("expenses.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def load_expenses():
    try:
        with open("expenses.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []

    expenses = []

    for item in data:
        expense = Expense(
            item["id"],
            item["category"],
            item["amount"],
            date.fromisoformat(item["date"])
        )
        expenses.append(expense)
    return expenses
