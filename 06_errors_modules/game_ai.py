# game_ai.py

import random
from game_util import turn



def computers_move(field, symbol): 
    """Returns the game field with a computers move.         
    'field' is the game field, on which we play, 
    'symbol' can be 'x' or 'o', according to which symbol the computer are playing with. """ 
    while True:
        try: 
            if '-oo' in field:  # the computer has advangtage
                position__oo = field.index('-oo')
                print(f'\tPosition_-oo = {position__oo}')
                new_field = turn(field, position__oo, symbol)
                return new_field

            elif 'oo-' in field:    # the computer has advantage
                position_oo_ = field.index('oo-')
                print(f'\tPosition_oo- = {position_oo_}')
                new_field = turn(field, position_oo_+3, symbol)
                return new_field

            elif 'x-x' in field:    # the player has advantage
                position_x_x = field.index('x-x')
                print(f'\tPosition_x-x = {position_x_x}')
                new_field = turn(field, position_x_x+1, symbol)
                return new_field

            elif '-xx' in field:    # the player has advantage
                position__xx = field.index('-xx')
                print(f'\tPosition_-xx = {position__xx}')
                new_field = turn(field, position__xx, symbol)
                return new_field

            elif 'xx-' in field:    # the player has advantage
                position_xx_ = field.index('xx-')
                print(f'\tPosition_xx- = {position_xx_}')
                new_field = turn(field, position_xx_+3, symbol)
                return new_field

            elif 'x--x' in field:    # the player has small advantage
                position_x__x = field.index('x--x')
                print(f'\tPosition_x--x = {position_x__x}')
                new_field = turn(field, position_x__x+1, symbol)
                return new_field

            elif '-x-' in field:    # the player has small advantage
                position__x_ = field.index('-x-')
                print(f'\tPosition_-x- = {position__x_}')
                new_field = turn(field, position__x_+2, symbol)
                return new_field
            
            elif '-o-' in field:    # the computer has small advantage
                position__o_ = field.index('-o-')
                print(f'\tPosition_-o- = {position__o_}')
                new_field = turn(field, position__o_, symbol)
                return new_field
    
            
            elif 'x' in field:    # the player played first
                #count_x = field.count('x')
                position_x = field.index('x')
                print(f'\tPosition_x = {position_x}')
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
                    print(f'\tPosition_xx = {position_xx}')
                    if field[position_xx - 1] == '-': 
                        new_field = turn(field, position_xx-1, symbol)
                        return new_field
                    elif field[position_xx + 1] == '-': 
                        new_field = turn(field, position_xx+1, symbol)
                        return new_field
                    else: 
                        position = random.randrange(0, 20)
                        print(f'\tRandom position: {position}')
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
            
        else: 
                        position = random.randrange(0, 20)
                        print(f'\tRandom position: {position}')
                        if field[position] == '-': 
                            new_field = turn(field, position, symbol)
                            return new_field

                            
        if '-' not in field: 
            raise ValueError('The field is full. ')