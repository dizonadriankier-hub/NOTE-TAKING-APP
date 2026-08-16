print("Welcome to simple taking notes\n")

notes_id = []
notes = {}

def add():
    note_id = int(input("Enter note ID: > "))
    note = input("Enter notes: > ")
    notes[note_id] = note


def edit():
    note_id = int(input("Enter note ID to edit: "))
    new_note = input("Enter new note: ")

    notes[note_id] = new_note
    print("Note Edited!\n")

while True:
    choice = int(input("1: To enter notes 2: To Exit 3: View Notes 4: Edit Notes\n> "))
    if choice == 1:
        add()
    elif choice == 3:
        print(notes)
    elif choice == 4:
        edit()
    else:
        break