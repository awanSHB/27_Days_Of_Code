keys = ['ten', 'twenty', 'thirty']
values = [10, 20, 30]
dictionary = dict(zip(keys, values))
print(dictionary)


print()
my_dict = {}
c = 0
for i in keys:
    my_dict[i] = values[c]
    c+=1
print(my_dict)


print()
for j in range(len(keys)):
    my_dict.update({keys[j]:values[j]})
print(my_dict)