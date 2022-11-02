# game_ai.py

import random
from game_util import turn



def computers_move(field, symbol): 
    """Returns the game field with a computers move.         
    'field' is the game field, on which we play, 
    'symbol' can be 'x' or 'o', according to which symbol the computer are playing with. """ 
    while True:
        try: 
            if 'x-x' in field:    # the player has advantage
                position_x_x = field.index('x-x')
                print(f'Position_x-x = {position_x_x}')
                new_field = turn(field, position_x_x+1, symbol)
                return new_field

            elif 'x--x' in field:    # the player has small advantage
                position_x__x = field.index('x--x')
                print(f'Position_x--x = {position_x__x}')
                new_field = turn(field, position_x__x+1, symbol)
                return new_field

            elif 'xx' in field:    # the player has advantage
                position_xx = field.index('xx')
                print(f'Position_xx = {position_xx}')
                if field[position_xx - 1] == '-': 
                    new_field = turn(field, position_xx-1, symbol)
                    return new_field
                elif field[position_xx + 2] == '-': 
                    new_field = turn(field, position_xx+2, symbol)
                    return new_field
                else: 
                    position = random.randrange(0, 20)
                    print(position)
                    if field[position] == '-': 
                        new_field = turn(field, position, symbol)
                        return new_field

            
            elif 'x' in field:    # the player played first
                count_x = field.count('x')
                position_x = field.index('x')
                print(f'Count_x = {count_x}\nPosition_x = {position_x}')
                if position_x == 0: 
                    new_field = turn(field, position_x+1, symbol)
                    return new_field
                elif position_x == 19: 
                    new_field = turn(field, position_x-1, symbol)
                    return new_field                
                elif field[position_x - 1] == '-': 
                    new_field = turn(field, position_x-1, symbol)
                    return new_field
                elif field[position_x + 1] == '-': 
                    new_field = turn(field, position_x+1, symbol)
                    return new_field
                else: 
                    position_xx = field.index('x', position_x+1)
                    print(f'Position_xx = {position_xx}')
                    if field[position_xx - 1] == '-': 
                        new_field = turn(field, position_xx-1, symbol)
                        return new_field
                    elif field[position_xx + 1] == '-': 
                        new_field = turn(field, position_xx+1, symbol)
                        return new_field
                    else: 
                        position = random.randrange(0, 20)
                        print(position)
                        if field[position] == '-': 
                            new_field = turn(field, position, symbol)
                            return new_field


        except ValueError: 
            position = random.randrange(0, 20)
            print(position)
            if field[position] == '-': 
                new_field = turn(field, position, symbol)
                return new_field

        except TypeError: 
            position = random.randrange(0, 20)
            print(position)
            if field[position] == '-': 
                new_field = turn(field, position, symbol)
                return new_field
            
        
        if '-' not in field: 
            raise ValueError('The field is full. ')