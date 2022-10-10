# swap.py

def swap_the_letter(word, position, letter): 
    """It takes a word, a position and a new letter and swap the letter to the position."""
    start = word[:position]
    end = word[position + 1:]
    return start + letter + end

word = input('Enter a word to swap: ')
position = int(input('Enter a position on which I will swap the letter: '))
letter = input('Enter a letter by which I will swap: ')

print('Nové slovo je: ', swap_the_letter(word, position, letter), '\n')


# initials: 
def initials(name, surname): 
    """It takes name and surname and return initials. """
    return name[0] + surname[0]


name = input('Enter name: ')
surname = input('Enter surname: ')
print('Initials are: ', initials(name, surname).upper())
