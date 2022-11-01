# game_piskvorky.py
from game_ai import computers_move
from game_util import turn

def rate_game(field): 
    """It evaluates the game. Returns 'x' for the x-winner,
                'o' for the o-winner, 
                '!' for the draw, 
                '-' for game is not over yet. """
    if 'xxx' in field: 
        return '"x" won! Congratulation. :-) '
    elif 'ooo' in field: 
        return '"o" won! Congratulation. :-) '
    elif '-' not in field: 
        return 'It is the draw! '
    else: 
        return '-'




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
                print(f'You cannot play to {position}. position! Try number 0–19. ')
            elif position > 19: 
                print(f'{position} is bigger than 19. You cannot play to this position! Please, try again. ')
            elif field[position] != '-':
                print(f'This position is full. Try again. ')
            else: 
                new_field = turn(field, position, symbol)
                return new_field



def piskvorky1d(): 
    """Makes the field. Call computers and players moves, print the game state and ends the game. """
    field = '-' * 20
    while '-' in field: 
        field = players_move(field, 'x')
        print(field)
        game_state = rate_game(field)
        if game_state == '-': 
            pass
        else: 
            print(game_state)
            break
        field = computers_move(field, 'o')
        print(field)
        game_state = rate_game(field)
        if game_state == '-': 
            pass
        else: 
            print(game_state)
            break


















