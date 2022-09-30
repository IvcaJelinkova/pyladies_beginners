#create a game stone, scissors, paper

from random import randrange

computers_move = randrange(3)
if computers_move == 0: 
    computers_move = 'stone'
elif computers_move == 1: 
    computers_move = 'scissors'
else: 
    computers_move = 'paper'

possible_stroke = ['stone', 'scissors', 'paper']
players_move = ''
while players_move not in possible_stroke: 
    players_move = input('What is your stroke? Type: "stone", "scissors" or "paper": ')
    if players_move not in possible_stroke: 
        continue
    elif computers_move == players_move: 
        print('Draw! ')     # remiza
    elif computers_move == 'stone': 
        if players_move == 'scissors': 
            print('The Computer wins! ')
        else: 
            print('You win! :-)')
    elif computers_move == 'scissors':
        if players_move == 'stone': 
            print('You win! :-D')
        else: 
            print('The Computer wins. ')
    elif computers_move == 'paper': 
        if players_move == 'stone': 
            print('The Computer wins... ')
        else: 
            print('You are the winner. :) ')


print('Computers move:', computers_move)
