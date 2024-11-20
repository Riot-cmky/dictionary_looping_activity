# Alright, let's simplify and rephrase the problem set to avoid using functions:
import student_data

# print(student_data.students)
students = student_data.students
# print(len(students))
# print(students[0]['Combo,Name'])
# print(students[0]['Email'][0])
# print(students[0]['Email'][1])
# print(students[0]["HR"])
# print(students[0]["GL"])




# for loops allow us to
#iterate through the data
#and perform some function

#we are iterating through the data
#and printing the name and email of the students
#we are also printing a line of underscores to separate the students
#we are also printing a line of underscores to separate the students
# for student in students:
#     print(student['Combo,Name'])
#     print(student['FName'])
#     print(student["MName"])
#     print(student["LName"])
#     print(student['Email'][0])
#     print(student['Email'][1])
#     print(student["HR"])
#     print("_"*25)


# we are asking the user to input their name
# then we are checking if the name is in the data
# if the name is in the data we are printing the name and "this works"
# name = input("what is you name?") 
# id = int(input("What is your id? "))
# for student in students:   # iterating thtough the students
#     if id == student['CPSID']:
#         print(student['Combo,Name'])
#         print("this works")


# # Let's try to print out the emails of the students:    

# email = input("what is you name? (Enter in this format Last, First)") 
# for student in students:
#     if name == student['Combo,Name']:
#         print(student['Email'][1])
       

#CRUD (Create - Read - Update - Delete)

# Update the dataset in memory (e.g., modify student details)
for student in students:
    if student['CPSID'] == 10000023:  # Example CPSID to update
        student['FName'] = 'Dom'
        student['LName'] = 'Toretto'
        student['GL'] = 11
        student['HR'] = "B129"



for student in students:
    if student['CPSID'] == 10000024:  # Replace with the condition to find the specific student
        del student['MName']  # Deletes the 'MName' key-value pair
        del student['GL']
        del student['HR']
        del student['Email'][0]
        del student['FName']
        del student['LName']
        print(f"Updated student: {student}")


# Update a specific entry by index
students[2]['FName'] = 'Jane'  # Updates the first student's first name
students[2]['LName'] = 'Doe'

print(students[2])

# Remove a specific student by index
del students[-1]  # Removes the first student in the list

# Example: Add a 'ContactNumber' field to each student
for student in students:
    student['ContactNumber'] = '123-456-7890'  # Assign a default or specific value

# Create a new student dictionary
new_student = {
    'CPSID': 987654,
    'Combo,Name': 'Doe, John',
    'FName': 'John',
    'LName': 'Doe',
    'MName': 'Paul',
    'HR': 'B220',
    'GL': 11,
    'Email': ['john.doe@example.com', 'j.doe@example.org']
}

# Add the new student to the list
students.append(new_student)


# Collecting input from the user for each field
cpsid = int(input("Enter CPSID: "))
combo_name = input("Enter Combo,Name (Last, First): ")
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
middle_name = input("Enter Middle Name: ")
homeroom = input("Enter Homeroom (e.g., B220): ")
grade_level = int(input("Enter Grade Level: "))
primary_email = input("Enter Primary Email: ")
secondary_email = input("Enter Secondary Email: ")
contact_number = input("Enter contact number: ")

# Create a new student dictionary using the input
new_student = {
    'CPSID': cpsid,
    'Combo,Name': combo_name,
    'FName': first_name,
    'LName': last_name,
    'MName': middle_name,
    'HR': homeroom,
    'GL': grade_level,
    'Email': [primary_email, secondary_email],
    'ContactNumber': contact_number
}

# Add the new student to the list
students.append(new_student)

# Print confirmation and the new student details
print("New student added:")
print(new_student)








# Overwrite the `student_data.py` file with the updated data
# Overwrite the student_data.py file with formatted data
with open('student_data.py', 'w') as f:
    f.write("students = [\n")
    for student in students:
        formatted_student = "    {\n"
        for key, value in student.items():
            formatted_student += f"        '{key}': {repr(value)},\n"
        formatted_student = formatted_student.rstrip(",\n") + "\n    },\n"  # Clean trailing commas and newline
        f.write(formatted_student)
    f.write("]\n")

print("student_data.py has been updated with the original formatting.")