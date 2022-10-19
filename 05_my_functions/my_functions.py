def yes_or_no(question):
    """Returns True or False according to the answer from the user. """
    while True: 
        answer = input(question).lower()
        if answer == 'yes': 
            return True
        elif answer == 'no': 
            return False
        else: 
            print('I do not understand! Answer "yes" or "no". ')

if yes_or_no('Do you want to play a game? '): 
    print('OK! But you have to write it. :-)\n')
else: 
    print('It is a pity.\n')


def sea_exploration(depth): 
    """Recursive function, which prints depth and if I'm in depth lower than 30, prints that I'm diving in. Than increases a depth and call itself. Otherwise I emerge. """
    print(f'I am looking around in depth {depth} m. ')
    if depth >= 30: 
        print('It\'s enough for me! ')
    else: 
        print(f'I\'m diving in (from {depth} m). ')
        sea_exploration(depth + 10)
        print(f'I\'m emerging (on {depth} m). ')

sea_exploration(0)

