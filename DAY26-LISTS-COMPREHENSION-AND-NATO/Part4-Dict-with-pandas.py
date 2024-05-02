import pandas

stu_dict = {
    'student': ['angela', 'alex', 'betty'],
    'score': [79, 60, 80]
}

student_data_frame = pandas.DataFrame(stu_dict)
print(student_data_frame)
print()

for (key, value) in student_data_frame.items():
    print(value)