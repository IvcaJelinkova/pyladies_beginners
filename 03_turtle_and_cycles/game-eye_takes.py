# you have 0 points and take the cards until you have 21 points
from random import randrange

score = 0
while True: 
    print('Your score: ', score)
    answer = input('Do you want to play? (yes/no): ').lower()
    if answer == 'no': 
        break
    elif answer != 'yes': 
        print('Don\'t know this answer. :-(')
        
    else: 
        card = randrange(2, 11)
        print('Your card: ', card)
        score += card
        if score > 21: 
            print('Game over. You lose! ')
            break

print('Your final score: ', score)

