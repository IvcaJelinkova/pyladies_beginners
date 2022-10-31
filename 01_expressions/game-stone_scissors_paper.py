#create a game stone, scissors, paper

from random import randrange

def computers_play(computers_move): 
    """Returns computers stroke. """
    if computers_move == 0: 
        return 'stone'
    elif computers_move == 1: 
        return 'scissors'
    else: 
        return 'paper'


def game_logic(computers_move, players_move): 
    """Returns the winner. """
    if computers_move == 'stone': 
        if players_move == 'scissors': 
            return 'The Computer! '
        else: 
            return 'You! :-)'
    elif computers_move == 'scissors':
        if players_move == 'stone': 
            return 'You! :-D'
        else: 
            return 'The Computer. '
    elif computers_move == 'paper': 
        if players_move == 'stone': 
            return 'The Computer'
        else: 
            return 'You. :) '


possible_stroke = ['stone', 'scissors', 'paper', 'end']
players_move = ''
while players_move != 'end':
    computers_move = computers_play(randrange(3))
    players_move = input('What is your stroke? Type: "stone", "scissors", "paper" or "end" for Game Over: ').lower()
    if players_move == 'end': 
        print('You ended this game. ')
        break
    elif players_move not in possible_stroke: 
        continue
    elif computers_move == players_move: 
        print('Draw! ')     # remiza
    else: 
        print('Computers move:', computers_move)
        print(f'\nTHE WINNER IS: {game_logic(computers_move, players_move)}')



