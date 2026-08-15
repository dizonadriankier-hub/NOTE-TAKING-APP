print("Welcome to simple taking notes")

notes = []

def add():
    note = input("Enter notes: ")
    notes.append(note)

while True:
    choice = int(input("1: To enter notes 2: To Exit 3: View Notes\n> "))
    if choice == 1:
        add()
    elif choice == 3:
        print(notes)
    else:
        break