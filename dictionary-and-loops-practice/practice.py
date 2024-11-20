import student_data

students = student_data.students

# 9. Seasrch for Students by last Names

# prompts user to enter last name
lastName = (input("What is your last name? "))
# when use inputs their last name, their other information will be printed
for student in students:
    if lastName == student['LName']:
        print(student["Combo,Name"])
        print(student["HR"])
        print(student["GL"])
        print(student["Email"][0])
        print(student["Email"][1])
    else:
        print('No student found with that last name.')
        print("_"*25) 
        break # prevent a bunch of repeats


# 10. List students in Mutiple Homerooms
homeroom = input("What is your homeroom? ")

for student in students:
    if homeroom == student['HR']["B21"]:
        print(student['Combo,Name'])
        print(student['HR'])
        print(student['Email'][0])
    else:
        print('No students found in the homerooms starting with B21')
        print("_"*25)
        break

# 11 Identify Students without middle names

# the system iterates through the students to see if they have a middle name
for student in students:
    if student['MName'] == '': # if the studnet name is blank it will be print its combo name
        print(student["Combo,Name"])
    else:
        print("All student have a middle name")
        print("_"*25)
        break # prevents a bunch of repeats