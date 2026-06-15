# to print out the highest score from the List......need to use what you have learnt about Lists, For Loops and Conditionals 
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

max_score = 0
for score in student_scores:
    if score >max_score:
       max_score = score
     
print(max_score)



sum = 0
for score in student_scores:
    sum += score
    
print(sum)
