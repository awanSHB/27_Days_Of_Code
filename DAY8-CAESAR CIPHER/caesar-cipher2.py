alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
'r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i',
'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(start_text,shift_amount, ciph_direction):
    end_text = ''
    if ciph_direction == 'decode':
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f'\nThe {ciph_direction}d text is  : :  {end_text}')
game_on_hai = True
while game_on_hai: 
    text = input("Enter the text : ")
    shift = int(input("Enter the shift : "))
    direction = input('What do you want with text "encode" or "decode" : ')
    caesar(start_text = text, shift_amount = shift, ciph_direction = direction)
    decision = input('\nIf you want to stop press "n" else press any key to continue : ')
    if decision == 'n':
        game_on_hai = False
        print("\t\t\t<!--GoodBye--!>")