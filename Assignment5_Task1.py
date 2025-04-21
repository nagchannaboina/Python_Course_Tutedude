# Create a Dictionary of Student Marks:

# A dictionary named student_marks which has student name and their marks.
student_marks = {'Alice': 85, 'Jack': 66, 'Mike': 96, 'Sam':90, 'James': 78, 'Altman': 25}

# i want to make the search with out case sensitivity
student_marks_lower = {key.lower(): value for key, value in student_marks.items()}

student_name = input('Enter the student\'s name : ')

if student_name in student_marks_lower:
    print('{}\'s marks: {}'.format(student_name.capitalize(), student_marks_lower[student_name]))
else:
    print('Student not found in the dictionary, please update it')
