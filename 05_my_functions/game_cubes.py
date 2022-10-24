""" TASK: 
1) 1. player rolls the dice until 6 falls. 
2) 2. player rools the dice until 6 falls. 
... 3. + 4. player also
4) Who wins? Who needed the most rools. If it is a draw – the one who played the first. 
"""

from random import randrange

def play_cubes(number_of_rolls, roll): 
    """Returns number of rolls by rolling six on the dice. """
    while roll != 6: 
        roll = randrange(1, 7)
        print(roll)
        number_of_rolls += 1
    return number_of_rolls


the_biggest = 0
winner = 0
for player in range(1, 5): 
    number_of_rolls = 0
    roll = 0
    number_of_rolls = play_cubes(number_of_rolls, roll)
    print(f'The {player}. player rolled 6 by {number_of_rolls} rolls. ')
    if number_of_rolls > the_biggest: 
        the_biggest = number_of_rolls
        winner = player

print(f'The {winner}. player won. \n')