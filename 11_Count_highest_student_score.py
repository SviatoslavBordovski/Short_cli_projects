# Example input => 78 65 89 86 55 91 64 89
# Example output => The highest score in the class is: 91
# Important note: it is restricted to use min() or max() functions

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_num = 0
# compare numbers
for num in student_scores:
  if num < highest_num:
    continue
  elif num > highest_num:
    highest_num = num

print("The highest score in the class is: ", highest_num)
