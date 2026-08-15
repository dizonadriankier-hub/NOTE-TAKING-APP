note_id = int(input("Enter note ID to edit: "))
new_title = input("Enter New Title: ")

for note in notes:
    if note["id"] == note_id:
        note["title"] = new_title
        print(f"Updated! (Original Author: {note['author']})")
        break
