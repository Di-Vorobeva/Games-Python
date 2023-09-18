from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

print('\nUse numbers to answer: 0 - No, 1 - Yes')
q1 = int(input('\nHow many passwords need to be generated: '))
q2 = int(input('How long should passwords be (no more than 32 symbols): '))
while q2 > 32:
    q2 = int(input('Please, no more than 32 symbols: '))
q3 = input('Need to include numbers {}? '.format(digits))
while q3 != '1' and q3 != '0':
    q3 = input('Yes - 1, no - 0, try again: ')
q4 = input('Need to include uppercase letters {}? '.format(uppercase_letters))
while q4 != '1' and q4 != '0':
    q4 = input('Yes - 1, no - 0, try again: ')
q5 = input('Need to include lowercase letters {}? '.format(lowercase_letters))
while q5 != '1' and q5 != '0':
    q5 = input('Yes - 1, no - 0, try again: ')
q6 = input('Need to include punctuation {}? '.format(punctuation))
while q6 != '1' and q6 != '0':
    q6 = input('Yes - 1, no - 0, try again: ')
q7 = input('Need to exclude ambiguos symbols "il1Lo0O"? ')
while q7 != '1' and q7 != '0':
    q7 = input('Yes - 1, no - 0, try again: ')

if q3 == '1':
    chars += digits
if q4 == '1':
    chars += uppercase_letters
if q5 == '1':
    chars += lowercase_letters
if q6 == '1':
    chars += punctuation
if q7 == '1':
    for c in 'il1Lo0O':
        chars.replace(c, '')


def generate_password(n):
    lenght = q2
    for i in range(n):
        print(''.join(sample(chars, lenght)))


print('\nPassword options:')
generate_password(q1)
