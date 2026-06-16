import json
from pathlib import Path

CREDS_FILE = Path("credentials.json")


def load_credentials():
    if CREDS_FILE.exists():
        with open(CREDS_FILE, 'r') as file:
            return json.load(file)
    return []


def save_credentials(credentials):
    with open(CREDS_FILE, 'w') as file:
        json.dump(credentials, file, indent=4)


def add_credential():
    credentials = load_credentials()
    website = input('Enter Website Name: ').lower().strip()
    if website == '':
        print('Website cannot be empty')
        return
    username = input('Enter Username: ').lower().strip()
    if username == '':
        print('Username cannot be empty')
        return
    password = input('Enter Password: ').strip()
    if len(password) < 6:
        print('Password must be at least 6 characters')
        return

    credential = {
        "website": website,
        "username": username,
        "password": password
    }
    credentials.append(credential)
    save_credentials(credentials)
    print('Credentials added successfully.')


def view_credentials(credentials):
    if not credentials:
        print('No credentials found.')
        return
    for creds in credentials:
        masked_password = "*" * len(creds["password"])
        print(f'{creds["website"]} | {creds["username"]} | {masked_password}')


def search_credential():
    credentials = load_credentials()
    search_website = input('Enter website: ').lower().strip()
    for creds in credentials:
        if (search_website == creds["website"]):
            print(f'{creds["website"]} \n{creds["username"]} \n{creds["password"]}')
            return
    print('Credentials not found.')


def delete_credential():
    credentials = load_credentials()
    cred_number = input('Enter credential number: ')
    if not cred_number.isdigit():
        print('Credential number must be a numeric value.')
        return

    cred_index = int(cred_number) - 1

    if cred_index < 0 or cred_index >= len(credentials):
        print('Invalid credential number.')
        return

    del credentials[cred_index]
    save_credentials(credentials)
    print('Credentials deleted successfully.')
    return


def show_menu():
    print("\n===== Password Manager =====")
    print("1. Add Credential")
    print("2. View Credentials")
    print("3. Search Credential")
    print("4. Delete Credential")
    print("5. Exit")


def main():
    while True:
        show_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_credential()

        elif choice == "2":
            credentials = load_credentials()
            view_credentials(credentials)

        elif choice == "3":
            search_credential()

        elif choice == "4":
            delete_credential()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 and 5.")


main()
