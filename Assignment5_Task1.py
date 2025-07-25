marks={'Swarup':76,'Pulak':70,'Binoy':73}
student=input("Enter the student's name: ")

if student in marks:
    print("{}'s marks:".format(student),marks[student])
else:
    print("Student not found.")
