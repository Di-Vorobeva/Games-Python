from random import *
word_list = ['accept', 'adapt', 'affect', 'afford', 'agree', 'always', 'answer', 'attract', 'attractive', 'bear', 'begin', 'borrow', 'bring',
             'broker', 'brokerage', 'budget', 'buyer', 'campus', 'case', 'civil', 'clock', 'close', 'company', 'computer', 'copy', 'count',
             'counter', 'cousin', 'cover', 'deal', 'dealer', 'debate', 'denial', 'difference', 'different', 'discovery', 'drive', 'duty',
             'ear', 'electronic', 'elite', 'email', 'emerge', 'enter', 'equal', 'equity', 'example', 'exchange', 'expire', 'face', 'facilitate',
             'father', 'fiber', 'field', 'fill', 'firm', 'flame', 'floor', 'flow', 'follow', 'forest', 'forget', 'form', 'formal', 'france',
             'frank', 'freely', 'frequently', 'friend', 'gear', 'gender', 'gene', 'gentry', 'give', 'good', 'grow', 'guarantor', 'hand',
             'haste', 'hear', 'hedge', 'heel', 'hide', 'hive', 'holy', 'home', 'home', 'honey', 'honour', 'hybrid', 'image', 'impact',
             'important', 'include', 'income', 'individual', 'insurance', 'interest', 'investor', 'joy', 'judge', 'king', 'knee', 'knife',
             'knock', 'know', 'know', 'known', 'lack', 'land', 'lap', 'large', 'large', 'larger', 'last', 'late', 'leave', 'lend',
             'like', 'likely', 'liquid', 'live', 'location', 'long', 'look', 'lord', 'love', 'maintain', 'make', 'map', 'margin',
             'mark', 'market', 'market', 'match', 'mean', 'method', 'minute', 'money', 'month', 'moral', 'move', 'multiple', 'nature',
             'nerve', 'network', 'note', 'obey', 'offer', 'open', 'oppose', 'order', 'ownership', 'paris', 'part', 'particular',
             'pension', 'physical', 'place', 'place', 'play', 'poor', 'porch', 'port', 'pose', 'post', 'potential', 'praise',
             'price', 'pride', 'program', 'proud', 'provide', 'purchase', 'purpose', 'quit', 'quote', 'range', 'real', 'recipe',
             'refuse', 'regard', 'rest', 'return', 'rich', 'role', 'room', 'royal', 'sale', 'say', 'scope', 'score', 'scream',
             'screen', 'script', 'security', 'seem', 'sell', 'seller', 'sense', 'serve', 'settlement', 'sick', 'similar',
             'small', 'snuff', 'speak', 'specific', 'speech', 'speedy', 'spread', 'stand', 'steal', 'stock', 'system',
             'tactic', 'tail', 'talent', 'talk', 'tape', 'time', 'tongue', 'trade', 'trader', 'transfer', 'true',
             'type', 'uncle', 'video', 'view', 'viewer', 'weapon', 'wear', 'week', 'well', 'will', 'wisdom', 'wish', 'word',
             'world', 'year', 'yell', 'yellow', 'young', 'youth']


def get_word():
    return choice(word_list).upper()


def display_hangman(tries):
    stages = [
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
        '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
        '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
        '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
        '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print('Let\'s play a game Hangman!')
    print(display_hangman(tries))
    print('Let me check, the word has {} letters\n'.format(
        len(word)), word_completion)
    while 0 < tries:
        attempt = input(
            '\nYour letter or the whole word: ').upper()
        while attempt.isalpha() != True:
            attempt = input(
                'Enter your letter or the whole word: ').upper()
        if attempt in guessed_letters:
            print('You\'ve already named this letter, try another one.')
            continue
        elif attempt in guessed_words:
            print('You\'ve already named this word, try another one.')
            continue
        if attempt not in word:
            tries -= 1
            if len(attempt) > 1:
                guessed_words.append(attempt)
            if len(attempt) == 1:
                guessed_letters.append(attempt)
            if tries == 0:
                print(display_hangman(tries))
            if tries > 0:
                print('No, you didn\'t guess. You have {} attempts left'.format(tries))
                print(display_hangman(tries))
        if word_completion == word or attempt == word:
            print('Congratulations! You got it right!')
            break
        if attempt in word:
            guessed_letters.append(attempt)
            for i in range(len(word)):
                if word[i] == attempt:
                    word_completion = word_completion[:i] + \
                        attempt + word_completion[i + 1:]
            print('Let\'s see how you\'re doing: ',
                  ''.join(word_completion).upper())
        if word == ''.join(word_completion).upper():
            print('Congratulations! You got the word - "{}"!'.format(word))
            break
    if tries == 0:
        print('Oops! You lose. The word was - "{}"'.format(word))


while True:
    play(get_word())
    if 'y' in input('\nDo you wanna play again? Yes/No  - ').lower():
        continue
    else:
        print('\nOkay, bye!')
    break
