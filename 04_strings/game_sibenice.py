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

guess_word = choice(['home', 'terminal', 'hermiona'])
word = len(guess_word) * '_ '
print(f'Your guessed word is: {word}.\n\t', guess_word)
tries = 9
tried_char = []

def swap(char, position, word): 
    """It swap char on given position in given word. """
    start = word[:position]
    middle = char + ' '
    end = word[position + 2:]
    return start + middle + end


while True: 
    char = input('Your guessed letter: ')
    if char in guess_word: 
        position = guess_word.index(char) * 2
        print(position+1)
        word = swap(char, position, word)
    else: 
        tries -= 1
        print(f'Number of remaining tries: {tries}. ')
        tried_char.append(char)
        if tries == 0: 
            print(f'You lost this game. Your wrong tries were: {tried_char}')
            break
    print(f'Your guessed word now looks like: {word}. ')

    if not '_' in word: 
        print('You won, congratulation. :-) ')
        break

    
    




