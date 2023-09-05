students_height = input("Enter the list of student's height : ").split()
for h in range(0, len(students_height)):
    students_height[h] = int(students_height[h])
print(students_height)

um = 0
elements = 0
k = 0
for k in students_height:
    um = um + k
    elements += 1
print("\nThe total heights are :>: ", um)
print("\nThe total students are :>: ", elements)
average_students = um/elements
print("\nThe average of students is :>: ", average_students)
print()

# Checking for the highest score in the list
stu_score = input("Enter the list of score in the class : ").split()
for h in range(0, len(stu_score)):
    stu_score[h] = int(stu_score[h])
print(stu_score)

high_score = 0
for score in stu_score:
    if score>high_score:
        high_score = score
print(f"The highest score in the class is :>: {high_score}")

