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


def edit():
    note_id = int(input("Enter note ID to edit: > "))

    if note_id in notes:
        new_note = input("Enter new note: > ")
        notes[note_id]["note"] = new_note
        new_author = input("Enter author's name: > ")
        notes[note_id]["author"] = new_author
        print("Note Edited!\n")
    else:
        print("Note ID not found!\n")


while True:
    choice = int(input(
        "1: Add Notes\n"
        "2: Exit\n"
        "3: View Notes\n"
        "4: Edit Notes\n"
        "> "
    ))

    if choice == 1:
        add()

    elif choice == 2:
        break

    elif choice == 3:
        for note_id, inner_dict in notes.items():
            print(f"Note ID: {note_id}")

            for key, value in inner_dict.items():
                print(f"   {key.capitalize()}: {value}\n")

    elif choice == 4:
        edit()

    else:
        print("Invalid choice!\n")