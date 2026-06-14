import json
from pathlib import Path

EXPENSES_FILE = Path("expenses.json")


def load_expenses():
    if EXPENSES_FILE.exists():
        with open(EXPENSES_FILE, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(EXPENSES_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():
    expenses = load_expenses()
    expenses_title = input("Enter your expense title: ").strip()
    expenses_amount = input("Enter amount: ").strip()

    if not expenses_amount.isdigit():
        print("Amount must be numeric.")
        return

    expenses_amount = int(expenses_amount)

    if expenses_amount <= 0:
        print("Amount must be greater than 0.")
        return

    expense = {
        "title": expenses_title,
        "amount": expenses_amount
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['title']} - Rs.{expense['amount']}")


def delete_expense():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    view_expenses(expenses)

    expense_no = input("Enter expense number to delete: ").strip()

    if not expense_no.isdigit():
        print("Expense number must be numeric.")
        return

    expense_index = int(expense_no) - 1

    if expense_index < 0 or expense_index >= len(expenses):
        print("Invalid expense number.")
        return

    del expenses[expense_index]
    save_expenses(expenses)
    print("Expense deleted successfully.")


def show_total_expenses():
    expenses = load_expenses()
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


def show_highest_expense():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    highest_expense = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest_expense["amount"]:
            highest_expense = expense

    print(f"Highest Expense: {highest_expense['title']} - Rs.{highest_expense['amount']}")


def show_menu():
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Show Total Expenses")
    print("5. Show Highest Expense")
    print("6. Exit")


def main():
    while True:
        show_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            expenses = load_expenses()
            view_expenses(expenses)

        elif choice == "3":
            delete_expense()

        elif choice == "4":
            print(f"Total Expenses: Rs.{show_total_expenses()}")

        elif choice == "5":
            show_highest_expense()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 and 6.")


main()