# 🚨 Count average student height without len() and sum() functions 👇
# Example input: 156 178 165 171 187

student_heights = input("Input a list of student heights\n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
  total_height += height

num_of_students = 0
for student in student_heights:
  num_of_students += 1

av_student_height = total_height/num_of_students
result = int(round(av_student_height, 0))

print(num_of_students)
print(total_height)
print(result)
