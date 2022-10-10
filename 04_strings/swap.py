# swap.py

def swap_the_letter(word, position, letter): 
    """It takes a word, a position and a new letter and swap the letter to the position."""
    start = word[:position]
    end = word[position + 1:]
    return start + letter + end

word = input('Enter a word to swap: ')
position = int(input('Enter a position on which I will swap the letter: '))
letter = input('Enter a letter by which I will swap: ')

print('Nové slovo je: ', swap_the_letter(word, position, letter))
