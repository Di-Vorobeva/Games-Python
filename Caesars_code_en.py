direction=input('\nSelect direction: encryption or descryption?\n').lower()
while direction != 'encryption' and direction != 'descryption':
    direction = input('Please, select between encryption and descryption\n').lower()
language=input('\nSelect language: russian or english?\n').lower()
while language != 'russian' and language != 'english':
    language = input('Please, select between russian and english \n').lower()
step=input('\nSelect step:\n')
while step not in '1234567890':
    step = input('Please, choose your step:\n').lower()
text=input('\nEnter your text:\n')
while text == '':
    text=input('\nEnter your text:\n')

def caesar_code(direction, language, step, text):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    for i in range(len(text)):
        if language == 'russian':
            alphas =32
            low_alphabet = rus_lower_alphabet
            upp_alphabet= rus_upper_alphabet
        if language == 'english':
            alphas = 26
            low_alphabet=eng_lower_alphabet
            upp_alphabet=eng_upper_alphabet
        if text[i].isalpha():
            if text[i] == text[i].lower():
                place = low_alphabet.index(text[i])
            if text[i] == text[i].upper():
                place = upp_alphabet.index(text[i])
            if direction == 'descryption':
                index = (place - int(step)) % alphas
            elif direction == 'encryption':
                index = (place + int(step)) % alphas
            if text[i] == text[i].lower():
                print(low_alphabet[index], end='')
            if text[i] == text[i].upper():
                print(upp_alphabet[index], end='')
        else:
            print(text[i],end='')

caesar_code(direction, language, step, text)