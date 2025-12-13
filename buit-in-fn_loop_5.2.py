# Sum
# Python has lots of built-in functions to help us work with numbers. One of them helps us calculate the sum (the total). e.g.
# student_scores = [180, 124, 165, 173,
# 189, 169, 146]
# total_score = sum(student_scores)
# But how does sum() work behind the scenes?

student_scores = [180, 124, 165, 173, 189, 169, 146]
inital= 0
for score in student_scores :
    inital += score
print(inital)

#or
student_scores = [180, 124, 165, 173, 189, 169, 146]
total_score = sum(student_scores)
print(total_score)

#max function
student_scores = [180, 124, 165, 173, 189, 169, 146]
highest_score = max(student_scores)

#or
student_scores = [180, 124, 165, 173, 189, 169, 146]
inital = 0
for score in student_scores :
    if score > inital :
        inital = score
print(inital)


