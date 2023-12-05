employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
my_dict = {}
res = dict.fromkeys(employees, defaults)
print(res)