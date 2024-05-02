#printing the squares of the numbers

num = [1, 2, 3, 4, 5, 6, 7]

sq_num = [n*n for n in num]

print(sq_num)
print()

name = "sohaib"
n_name = [num for num in name]
print(n_name)
print()

numbers = [1, 1, 2, 3, 5, 8, 13, 33, 34, 35]
new_num = [num for num in numbers if num%2==0]
print(new_num)
print()