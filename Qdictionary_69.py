
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores. 
# Write a program that converts their scores to grades
# By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values.
# The final version of the student_grades dictionary will be checked. 
# **DO NOT** modify lines 1-7 to change the existing student_scores dictionary. 
# This is the scoring criteria: 
# - Scores 91 - 100: Grade = "Outstanding" 
# - Scores 81 - 90: Grade = "Exceeds Expctations" 

# - Scores 71 - 80: Grade = "Acceptable" 
# - Scores 70 or lower: Grade = "Fail" 

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

for student in student_scores:
    score = student_scores[student]
    if score >= 91 :
        print(f"{student} : grade A")
    elif score >= 81 :
        print(f"{student} : grade B")
    elif score >= 71 :
        print(f"{student} : grade C")
    elif score >= 61 :
        print(f"{student} : grade D")
    else:
        print(f"{student} : grade F")


####------------or----------------

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
 
# Create an empty dictionary to collect the new values.
student_grades = {}
 
# Loop through each key in the student_scores dictionary
for student in student_scores:
 
    #Get the value (student score) by using the key each time.
    score = student_scores[student]
 
    #Check what grade the score would get, then add it to student_grades
    if score >= 91:
        student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'
 
 



