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
    print('OK! But you have to write it. :-) ')
else: 
    print('It is a pity. ')
