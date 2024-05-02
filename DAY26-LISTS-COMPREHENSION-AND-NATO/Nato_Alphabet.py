import pandas

data = pandas.read_csv('phonet.csv')
# print(data)
# print()

phonetic_dict = {row.letter: row.code for(index, row) in data.iterrows()}
# print(phonetic_dict)
# print()

word = input("Enter the word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)