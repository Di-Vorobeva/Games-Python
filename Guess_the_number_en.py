from random import *
phrase_noncorrect = ['Please, enter numbers']
phrases_so_tiny = ['Your number less than mine!', 'Take some more!',
                   'Need a bigger one!']
phrases_too_much = ['So big number!',
                    'Your number bigger tha mine!', 'Take some less!']
phrases_you_are_right = [
    'Yes, you are right! ', 'Good job, this is it!']
print('\nWelcome to the "Guess the number"! I will pick a number and you need to guess. \n',
      '\nYou can choose a range from 1 to infinity', sep='')


def is_valid(num):
    return num.isdigit() and 1 <= int(num)


def is_valid_num():
    while True:
        num = input('\nYour number:')
        if is_valid(num):
            return int(num)
        else:
            print(''.join(phrase_noncorrect))


def game_body():
    print('\nWhat range do you prefer? Enter two numbers each on a new line')
    x, y = int(input()), int(input())
    if x > y:
        x, y = y, x
    s = randint(x, y)
    counter = 0
    while True:
        n = is_valid_num()
        counter += 1
        if n < s:
            print(choice(phrases_so_tiny))
        elif n > s:
            print(choice(phrases_too_much))
        elif n == s:
            print(choice(phrases_you_are_right))
            print('\nNumber of tries:', counter)
            break


while True:
    game_body()
    if 'y' in input('\nDo you wanna play again? Y/N?  - ').lower():
        continue
    else:
        print('\nOkay, bye!')
    break
