student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
for key in student_scores:
        # print(student_scores[key])

    score = student_scores[key]
    if score > 90 and score < 100:
        student_scores[key] = "Outstanding"
    elif score >= 81 and score < 90:
        student_scores[key] = "Exceeds Expectations"
    elif score >= 71 and score < 80:
        student_scores[key] = "Acceptable"
    elif score < 70:
        student_scores[key] = "Fail"
print(student_scores)

    
    
    
    



#TODO-2: Write your code below to add the grades to student_grades.👇

    

# 🚨 Don't change the code below 👇
# print(student_grades)