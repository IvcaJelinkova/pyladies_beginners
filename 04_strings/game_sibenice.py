# small steps: 
    # nb picks one word
    # nb prints this word from '_ '
    # players input a letter
    # nb evaluates this try --> change '_ ' to the letter or increases wrong tries
    # nb prints the word 
    # if there is no '_ ' --> congrats to player and game is over
    # nb prints the count of wrong tries
    # if the count of wrong tries >= 9: the player loose and game is over


from random import choice
from game_sibenice_picture import picture

def yes_or_no(question): 
    """Returns True when user insert 'yes/y', otherwise returns False. """
    answer = input(f'{question}: ').lower()
    if answer == 'yes' or answer == 'y': 
        return True
    elif answer == 'no' or answer == 'n': 
        return False
    else: 
        print('Sorry, I don\'t understand. ')
        return yes_or_no('Do you want to play a game? ')


def swap(char, position, word): 
    """It swap char on given position in given word. """
    start = word[:position]
    middle = char + ' '
    end = word[position + 2:]
    return start + middle + end

def __game_sibenice_(): 
    guess_word = choice(['home', 'terminal', 'hermiona', 'chocolate', 'sleep'])
    word = len(guess_word) * '_ '
    print(f'Your guessed word is: {word}.\n\t')
    tries = 10
    tried_char = []

    while True: 
        char = input('Your guessed letter: ').lower().strip()
        if len(char) == 1 and char.isalpha(): 
            if char in guess_word: 
                quantity_of_char = guess_word.count(char)
                if quantity_of_char > 1: 
                    position = -1
                    #for multiple-appereance of char: 
                    for quantity in range(quantity_of_char): 
                        position = guess_word.index(char, position + 1) * 2
                        word = swap(char, position, word)
                        position = int(position / 2)
                else: 
                    position = guess_word.index(char) * 2
                    word = swap(char, position, word)
            else: 
                tries -= 1
                print(f'Number of remaining tries: {tries}. ')
                print(picture(9-tries))
                tried_char.append(char)
                if tries == 0: 
                    print(f'You lost this game. Your wrong tries were: {tried_char}')
                    break
            print(f'Your guessed word now looks like: {word}.\n')
        else: 
            print('Please, write one letter!')

        if not '_' in word: 
            print('You won, congratulation. :-) ')
            break

        
while True: 
    if yes_or_no('Do you want to play a game? '): 
        __game_sibenice_()
    else: 
        print('OK, bye. ')
        break

