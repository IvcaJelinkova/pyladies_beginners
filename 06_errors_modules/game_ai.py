# game_ai.py

import random
from game_util import turn



def computers_move(field, symbol): 
    """Returns the game field with a computers move.         
    'field' is the game field, on which we play, 
    'symbol' can be 'x' or 'o', according to which symbol the computer are playing with. """ 
    while True:
        position = random.randrange(0, 20)
        print(position)
        if field[position] == '-': 
            new_field = turn(field, position, symbol)
            return new_field
        if '-' not in field: 
            raise ValueError('The field is full. ')