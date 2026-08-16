def edit(notes):
    note_id = int(input("Enter note ID to edit: > "))

    if note_id in notes:
        print(f"Current note: {notes[note_id]['note']}")
        print(f"Current author: {notes[note_id]['author']}")

        new_note = input("Enter new note: > ")

        notes[note_id]["note"] = new_note

        print("Note Edited!\n")

    else:
        print("Note ID not found!\n")