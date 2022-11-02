# game_util.py


def turn(field, position, symbol): 
    """Returns the game field with new symbol situated in the given positon. 
    'field' is the game field, on which we play, 
    'position' is the number of field, starts from 0 to 19, 
    'symbol' can be 'x' or 'o', according to which symbol the player are playing with. """
    if 0<=position<20:
        if symbol == 'x' or symbol == 'o': 
            if field[position] == '-': 
                start = field[:position]
                end = field[position+1:]
                new_field = start+symbol+end
                return new_field
            else: 
                raise ValueError(f'You cannot play to this position. Field number {position}. is full now. ')
        else: 
            raise ValueError(f'You cannot play with "{symbol}". Insert "x" or "o". ')
    raise ValueError(f'You cannot play to {position}. Insert the number from 0 to 19. ')
