import json
from pathlib import Path

CONTACTS_FILE = Path("contacts.json")

def load_contacts():
    if CONTACTS_FILE.exists():
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ").strip().lower()
    number = input("Enter number: ").strip()

    if not number.isdigit():
        print("Phone number should contain digits only.")
        return

    contacts[name] = number
    save_contacts(contacts)
    print("Contact added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    for name, number in contacts.items():
        print(f"{name.title()}: {number}")

def search_contact(contacts):
    name = input("Search contact: ").strip().lower()

    if name in contacts:
        print(f"{name.title()}: {contacts[name]}")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter contact name to delete: ").strip().lower()

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def show_menu():
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def main():
    contacts = load_contacts()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid option. Please choose between 1 and 5.")
main()