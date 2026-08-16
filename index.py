print("Welcome to Simple Note Taking\n")

from edit import edit
from person import view_notes
from delete import delete

notes = {}


def add():
    note_id = int(input("Enter note ID: > "))
    author = input("Enter author: > ")
    note = input("Enter note: > ")

    notes[note_id] = {
        "author": author,
        "note": note
    }

    print("Note Added!\n")


while True:
    choice = int(input(
        "1: Add Notes\n"
        "2: Exit\n"
        "3: View Notes\n"
        "4: Edit Notes\n"
        "5: Delete Notes\n"
        "> "
    ))

    if choice == 1:
        add()

    elif choice == 2:
        print("Goodbye!")
        break

    elif choice == 3:
        view_notes(notes)

    elif choice == 4:
        edit(notes)

    elif choice == 5:
        delete(notes)

    else:
        print("Invalid choice!\n")