import random

#Dictionary comprehension
names = ['Alex', 'Beth', 'calcy', 'caroline', 'dave']
dict_of_list = {student: random.randint(0,100) for student in names}
print(dict_of_list)

#Checking for the passes students
passed_students = {student: score for (student , score) in dict_of_list.items() if score >=60}
print(passed_students)
print()

#Taking the sentence and then converting it into list by splitting its words and then to dictionary
sentence = "what is the Airspeed velocity of an unladon swallow"
abc = sentence.split()
print(abc)
abc = {sin: len(sin) for sin in abc}    #printing the number of characters in each word
print(abc)
print()

# Converting the days temperature from celcius to fahrenheit
days = {
    'monday': 20,
    'tuesday': 24,
    'wednesday': 28,
    'thursday': 32,
    'friday': 36,
    'saturday': 40,
    'sunday': 44,
}

to_fahrenheit = {day: (temp_c*9/5)+32 for (day, temp_c) in days.items()}
print(to_fahrenheit)
