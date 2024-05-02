with open('Book.csv') as data_file:
    data = data_file.readlines()
    for row in data:
        print(row)



import pandas
data = pandas.read_csv('Book.csv')
print(data)