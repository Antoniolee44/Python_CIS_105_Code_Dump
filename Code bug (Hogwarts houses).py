student_data = dict(Jason='Gryffindor', Kaitlynne="Ravenclaw", Nicole='Hufflepuff', Antonio='Gryffindor',
                    Alexander='Ravenclaw', Samantha='Slytherin', Reagan='Hufflepuff', Luaren='Gryffindor',
                    Emma='Ravenclaw', Veronica='Slytherin', Matthew='Hufflepuff', Madison='Gryffindor',
                    Cedric='Gryffindor', Jijoy='Ravenclaw', Alex='Hufflepuff', Christopher='Slytherin')


def Print():
    pass


Print()
for student, house in student_data.items():
    if 'Gryffindor' == house:
        print(student)
