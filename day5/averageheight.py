# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#print(student_heights)
#Write your code below this row 👇
#print(type(student_heights))
t = 0
j = 0 
for i in student_heights:
  #sum = t + i
  t += i
  j += 1
#print(j)
#print(sum)
average = t / j
print(round(average))