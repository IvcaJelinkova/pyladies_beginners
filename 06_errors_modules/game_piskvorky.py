def rate_game(field): 
    """It evaluates the game. Returns 'x' for the x-winner,
                'o' for the o-winner, 
                '!' for the draw, 
                '-' for game is not over yet. """
    if 'xxx' in field: 
        return 'x'
    elif 'ooo' in field: 
        return 'o'
    elif '-' not in field: 
        return '!'
    else: 
        return '-'


def turn(field, position, symbol): 
    """Returns the game field with new symbol situated in the given positon. 
    'field' is the game field, on which we play, 
    'position' is the number of field, starts from 0 to 19, 
    'symbol' can be 'x' or 'o', according to which symbol the player are playing with. """
    if 0<=position<20:
        if field[position] == '-': 
            if symbol in 'xo': 
                start = field[:position]
                end = field[position+1:]
                new_field = start+symbol+end
                return new_field
            else: 
                raise ValueError(f'You cannot play with "{symbol}". Insert "x" or "o". ')
        else: 
            raise ValueError(f'You cannot play to this position. Field number {position}. is full now. ')
    raise ValueError(f'You cannot play to {position}. Insert the number from 0 to 19. ')


def players_move(field, symbol): 
    """Asks the player to its move and returns new field. 
    'field' is the game field, on which we play, 
    'symbol' can be 'x' or 'o', according to which symbol the player are playing with. """
    while True: 
        input_position = input('To which position you want to play? ')
        try: 
            position = int(input_position)
        except ValueError: 
            print('This is not a number. Please, try again. ')
        else: 
            if position < 0: 
                print(f'{position} is smaller than 0. You cannot play to this position! Try again. ')
            elif position > 19: 
                print(f'{position} is bigger than 19. You cannot play to this position! Please, try again. ')
            elif field[position] != '-':
                print(f'This position is full. Try again. ')
            else: 
                new_field = turn(field, position, symbol)
                return new_field

#print(players_move('o-------------------', 'x'))
        













