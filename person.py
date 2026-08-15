





#EDIT
note_id = int(input("Enter note ID to edit: "))
new_title = input("Enter New Title: ")

for note in notes:
    if note["id"] == note_id:
        note["title"] = new_title
        print(f"Updated! (Original Author: {note['author']})")
        break






#VIEW PERSON
def view_notes(notes):
    if len (notes) == 0:
       print("No notes available")
       return

    print("\n====VIEW NOTES====")   
    for i, note in enumerate(notes, 1):
        print(f"\nNote #{1}")
        print(f"Created by: {note['name']}")
        print(f"Note: {note['note']}")
    