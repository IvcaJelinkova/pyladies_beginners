from game_piskvorky import rate_game, players_move
from game_util import turn
import pytest

def test_rate_game(): 
    """Will test function rate_game. """
    assert rate_game('-----------') == '-'
    assert rate_game('--o--xxx------') == '"x" won! Congratulation. :-) '
    assert rate_game('xoxoxoxoxoxxooxo') == 'It is the draw! '
    assert rate_game('---ooo--') == '"o" won! Congratulation. :-) '

def test_turn(): 
    """Will test function turn. """
    assert turn('--------------------', 0, 'x') == 'x-------------------'
    assert turn('--------------------', 19, 'o') == '-------------------o'
    assert turn('x-o-x-o-x-o-x-o-x-o-', 5, 'x') == 'x-o-xxo-x-o-x-o-x-o-'

def test_bad_turn(): 
    """Will test bad turn. """
    with pytest.raises(ValueError): 
        turn('--------------------', -1, 'x')
        turn('x-------------------', 0, 'o')
        turn('--------------------', 0, 'potato')



#def test_allowed_players_move(): 
    """Will test allowed players move. """ """ 
    assert players_move('--------------------', 'o')
    pass

def test_not_allowed_players_move():  """  
    """Will test not allowed players move. """
    pass


#def test_computers_move(): 
    #""" """
    #assert computers_move('o-------------------', 'x') == ''
    #pass #random cannot be tested

