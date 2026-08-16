print("Welcome to Simple Note Taking\n")

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
        break

    elif choice == 3:
        print("View feature will be added later.\n")

    elif choice == 4:
        print("Edit feature will be added later.\n")

    elif choice == 5:
        print("Delete feature will be added later.\n")

    else:
        print("Invalid choice!\n")