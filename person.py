def view_notes(notes):
    if len (notes) == 0:
       print("No notes available")
       return

    print("\n====VIEW NOTES====")   
    for i, note in enumerate(notes, 1):
        print(f"\nNote #{1}")
        print(f"Created by: {note['name']}")
        print(f"Note: {note['note']}")
    