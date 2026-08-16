def view_notes(notes):
    if len(notes) == 0:
        print("No notes available.\n")
        return

    print("\n===== VIEW NOTES =====")

    for note_id, note in notes.items():
        print(f"ID: {note_id}")
        print(f"Created by: {note['author']}")
        print(f"Note: {note['note']}")
        print()