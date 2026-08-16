#Create Delete Function

def delete(notes):
    note_id = int(input("Enter note ID to delete: > "))

    if note_id in notes:
        del notes[note_id]
        print("Note Deleted!\n")

    else:
        print("Note ID not found!\n")