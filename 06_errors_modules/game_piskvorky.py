def rate_game(field): 
    """Returns 'x' for the x-winner,
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
                return start+symbol+end
            else: 
                raise ValueError(f'You cannot play with {symbol}. Insert "x" or "o". ')
        else: 
            raise ValueError(f'You cannot play to this position. Field number {position}. is full now. ')
    raise ValueError(f'You cannot play to {position}. Insert the number from 0 to 19. ')









