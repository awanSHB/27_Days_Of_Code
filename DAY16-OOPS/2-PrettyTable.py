from prettytable import PrettyTable
# setting the object as table and constructing it from a class
table = PrettyTable()
table.add_column("Student", ['Qasim', 'Ali', 'Umair'])
table.add_column("MARKS", ['80', '50', '70'])

print(table)