students = {'Hermione': 'Gryffindor',
            'Harry': 'Gryffindor',
            'Ron': 'Gryffindor',
            'Draco': 'Slitherin',
            }
name = input("what's your name?")

# old school
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("who da fauq are you?")

# New School of an if loop
match name:
    case "Harry" | "Hermione" | "Ron":
        print("First Year")
    case "Draco":
        print("First Year")
    case _:
        print("No idea")
