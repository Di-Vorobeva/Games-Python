from random import *
answers = ['It is certain', 'It is decidely so', 'Without a doubt', 'Yes - definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs pont to yes', 'Reply hazy, try again',
           'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Do not count on it', 'My reply is no', 'My sourses say no', 'Outlook not so good', 'Very doubtful']

print('\nHi! I am a Magic eight ball.\n', 'I see, you are here because you need an answer.\n',
      "\nLet's start with my questions: what's your name? ", sep='')
name = input('Your name: ')
print('\nNice to meet you, ', name, '!', sep='')


def game():
    while True:
        print('\nSo, what is your question?')
        que = input()
        if que != '' and '?' in que:
            print(choice(answers))
            break
        else:
            print('\nPlease, enter your question.')
            continue


while True:
    game()
    if 'y' in input('\nDo you wanna play again? Y/N?  - ').lower():
        continue
    else:
        print('\nOkay, so be content with what you have!')
    break
