print('This is first method')

file = open('first.txt')
content = file.read()
print(content)

print()
#------Another Method-------
print('This is second method')

with open('first.txt') as file:
    content = file.read()
    print(content)
print()
#------Writing in the file

with open('first.txt', mode='a') as file:   # the 'a' will append the text not delete it
    file.write("\nI am a student")
print()

with open('second.txt', mode='w') as file:  # this file does not exists, works only in 'w' mode
    file.write("This is going to be great") # new  file is created automatically