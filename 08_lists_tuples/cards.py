import random 

def make_a_deck_of_cards(): 
    """Returns new shuffled list of playing cards for game Prší. 
    The deck contains tuple – value-color. 
    Values of cards are: 2–10 and J, Q, K, A. 
    Colors are '♥' '♦' '♠' '♣'. """
    deck_of_cards = []
    shuffled_deck_of_cards = []
    values_of_cards = list(range(2, 11))
    letters_of_cards = list('JQKA')

    for color in '♥' '♦' '♠' '♣': 
        for value in values_of_cards + letters_of_cards: 
            tuple = (str(value), color)
            deck_of_cards.append(tuple)
            tuple = ''
    shuffled_deck_of_cards = random.sample(deck_of_cards, len(deck_of_cards))

    return shuffled_deck_of_cards

print((make_a_deck_of_cards()))


