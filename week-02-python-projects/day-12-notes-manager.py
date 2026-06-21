import json
from pathlib import Path

NOTES_FILE = Path("notes.json")


def load_notes():
    if NOTES_FILE.exists():
        with open(NOTES_FILE, 'r') as file:
            return json.load(file)
    return []


def save_notes(notes):
    with open(NOTES_FILE, 'w') as file:
        json.dump(notes, file, indent=4)


def add_note():
    notes = load_notes()
    note_title = input('Title: ').lower().strip()
    if not note_title:
        print('Title cannot be empty')
        return
    note_content = input('Content: ').lower().strip()
    if not note_content:
        print('Content cannot be empty')
        return

    note = {
        "title": note_title,
        "content": note_content
    }
    notes.append(note)
    save_notes(notes)
    print('Note saved successfully')


def view_notes(notes):
    if not notes:
        print('Notes not found')
        return
    for index, note in enumerate(notes, start=1):
        print(f'{index}. {note["title"]}\n{note["content"]}')


def search_note():
    notes = load_notes()
    search_title = input('Enter Title: ').lower().strip()
    for note in notes:
        if search_title == note["title"]:
            print(f'{note["title"]}\n{note["content"]}')
            return
    print('Note does not exist!')


def edit_note():
    notes = load_notes()
    edit_title = input("Enter Note Title to Edit: ").strip().lower()
    for note in notes:
        if edit_title == note["title"]:
            new_title = input("Enter New Title: ").strip().lower()
            new_content = input("Enter New Content: ").strip().lower()
            if not new_title:
                print("Title cannot be empty.")
                return
            if not new_content:
                print("Content cannot be empty.")
                return
            note["title"] = new_title
            note["content"] = new_content

            save_notes(notes)
            print("Note updated successfully.")
            return
    print("Note does not exist.")


def delete_note():
    notes = load_notes()
    note_num = input("Enter Note Number to Delete: ")
    if not note_num.isdigit():
        print("Note number must be a numeric value.")
        return
    note_index = int(note_num) - 1
    if note_index < 0 or note_index >= len(notes):
        print("Incorrect Note Number.")
        return
    del notes[note_index]
    save_notes(notes)
    print("Note deleted successfully.")


def main_menu():
    menu = '''
===== Notes Manager =====

1. Add Note
2. View Notes
3. Search Note
4. Edit Note
5. Delete Note
6. Exit
'''
    print(menu)


def main():
    while True:
        main_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_note()

        elif choice == "2":
            notes = load_notes()
            view_notes(notes)

        elif choice == "3":
            search_note()

        elif choice == "4":
            edit_note()

        elif choice == "5":
            delete_note()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 and 6.")


main()