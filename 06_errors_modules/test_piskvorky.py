import pytest
import builtins

# Tady by normálně byly importy (např. "from game_piskvorky import rate_game").
# Aby základní testy fungovaly i když některé moduly ještě nejsou napsané,
# jsou importy až v testovacích funkcích. To se normálně nedělá.

@pytest.mark.level(1)
def test_import_rate_game():
    """Function game_piskvorky.rate_game can be imported. """
    from game_piskvorky import rate_game


@pytest.mark.level(2)
def test_rate_game_x_won():
    """Crosses won. """
    from game_piskvorky import rate_game
    assert rate_game('xxx-----------------') == '"x" won! Congratulation. :-) '


@pytest.mark.level(2)
def test_rate_game_o_won():
    """'o' won. """
    from game_piskvorky import rate_game
    assert rate_game('ooo-----------------') == '"o" won! Congratulation. :-) '


@pytest.mark.level(3)
def test_rate_game_draw():
    """It is a draw!"""
    from game_piskvorky import rate_game
    assert rate_game('oxoxoxoxoxoxoxoxoxox') == 'It is the draw! '
    assert rate_game('xxooxxooxxooxxooxxoo') == 'It is the draw! '


@pytest.mark.level(4)
def test_rate_game():
    """Play did not over. """
    from game_piskvorky import rate_game
    assert rate_game('xx----------------oo') == '-'
    assert rate_game('-xoxoxoxoxoxoxoxoxox') == '-'
    assert rate_game('-xooxxooxxooxxooxxoo') == '-'
    assert rate_game('xoxoxoxoxoxoxoxoxox-') == '-'
    assert rate_game('xooxxooxxooxxooxxoo-') == '-'
    assert rate_game('oxoxoxoxo-oxoxoxoxox') == '-'
    assert rate_game('xxooxxoox-ooxxooxxoo') == '-'


@pytest.mark.level(10)
def test_import_turn():
    """Function game_util.turn can be imported. """
    from game_util import turn


@pytest.mark.level(11)
def test_turn_x():
    """Positive test of the function `turn` with symbol 'x'"""
    from game_util import turn
    assert turn("--------------------", 0, 'x') == 'x-------------------'
    assert turn("--------------------", 10, 'x') == '----------x---------'
    assert turn("--------------------", 19, 'x') == '-------------------x'
    assert turn("o-ox----------------", 1, 'x') == 'oxox----------------'


@pytest.mark.level(11)
def test_turn_o():
    """Positive test of the function `turn` with symbol 'o'"""
    from game_util import turn
    assert turn("--------------------", 0, 'o') == 'o-------------------'
    assert turn("--------------------", 10, 'o') == '----------o---------'
    assert turn("--------------------", 19, 'o') == '-------------------o'
    assert turn("x-xo----------------", 1, 'o') == 'xoxo----------------'


@pytest.mark.level(20)
def test_turn_big_position():
    """turn to the position which is not in the field could end with ValueError. """
    from game_util import turn
    with pytest.raises(ValueError):
        turn("--------------------", 20, 'x')


@pytest.mark.level(21)
def test_turn_negative_position():
    """turn to the negative position could end with ValueError. """
    from game_util import turn
    with pytest.raises(ValueError):
        turn("--------------------", -1, 'x')


@pytest.mark.level(22)
def test_turn_occupied():
    """turn to the occupied field could end with ValueError"""
    from game_util import turn
    with pytest.raises(ValueError):
        turn("o-------------------", 0, 'o')
    with pytest.raises(ValueError):
        turn("----------x---------", 10, 'o')


@pytest.mark.level(23)
def test_turn_wrong_symbol():
    """turn with different symbol than 'o' or 'x' could end with ValueError"""
    from game_util import turn
    with pytest.raises(ValueError):
        turn("--------------------", 2, 'řeřicha')
    with pytest.raises(ValueError):
        turn("--------------------", 2, 'm')
    with pytest.raises(ValueError):
        turn("--------------------", 2, '')


@pytest.mark.level(24)
def test_turn_small_characters():
    """Symbols 'o' a 'x' have to be small characters. """
    from game_util import turn
    with pytest.raises(ValueError):
        turn("--------------------", 2, 'O')
    with pytest.raises(ValueError):
        turn("--------------------", 2, 'X')


@pytest.mark.level(24)
def test_turn_wrong_symbol_ox():
    """turn with more symbols togetger could end with ValueError"""
    from game_util import turn
    with pytest.raises(ValueError):
        turn("--------------------", 2, 'xo')
    with pytest.raises(ValueError):
        turn("--------------------", 2, 'ox')


@pytest.mark.level(30)
def test_import_turn_of_player():
    from game_piskvorky import players_move


@pytest.mark.level(31)
def test_players_move_x_0(push_input):
    """turn of the player: X to the position 0 on the empty field. """
    from game_piskvorky import players_move
    push_input('0')
    assert players_move('--------------------', 'x') == 'x-------------------'


@pytest.mark.level(31)
def test_players_move_o_19(push_input):
    """turn hráče: O na pozici 19 na prázdné field"""
    from game_piskvorky import players_move
    push_input('19')
    assert players_move('--------------------', 'o') == '-------------------o'


@pytest.mark.level(32)
def test_players_move_not_number(push_input):
    """turn of the player: answer 'řeřicha' is not corrected, will ask again. """
    from game_piskvorky import players_move
    push_input('řeřicha', '2')
    assert players_move('--------------------', 'o') == '--o-----------------'


@pytest.mark.level(33)
def test_players_move_occupied(push_input):
    """turn of the player: full field is not corrected, will ask again. """
    from game_piskvorky import players_move
    push_input('0', '1')
    assert players_move('x-------------------', 'o') == 'xo------------------'


@pytest.mark.level(34)
def test_players_move_example(push_input):
    """turn of the player: test of the example from the entry. """
    from game_piskvorky import players_move
    push_input('don\t know', '0', '-1', '151', '2')
    assert players_move('o-------------------', 'x') == 'o-x-----------------'


@pytest.mark.level(40)
def test_import_computers_turn():
    from game_ai import computers_move


@pytest.mark.level(41)
def test_computers_move_prazdne():
    """turn of the computer on the empty field"""
    from game_ai import computers_move
    for symbol in 'ox':
        result = computers_move('-' * 20, symbol)
        assert len(result) == 20, result + ': Wrong lengt of the field'
        assert result.count('-') == 19, result + ': Wrong number of dashes'
        assert result.count(symbol) == 1, result + ': Wrong number of symbols ' + symbol


@pytest.mark.level(42)
def test_computers_move_full():
    """turn of the computer to the full field have to raise ValueError"""
    from game_ai import computers_move
    for symbol in 'ox':
        with pytest.raises(ValueError):
            result = computers_move('x' * 20, symbol)


@pytest.mark.level(43)
def test_computers_move_almost_full():
    """turn of the computer on almost full field (free in the middle)"""
    from game_ai import computers_move
    field = 'xoxoxoxoxo-xoxoxoxox'
    result = computers_move(field, 'o')
    # There is only one possibility to which field play.
    assert result == 'xoxoxoxoxooxoxoxoxox'


@pytest.mark.level(43)
def test_computers_move_almost_full_start():
    """turn of the computer to almost full field (free in the start)"""
    from game_ai import computers_move
    field = '-xoxoxoxoxoxoxoxoxox'
    result = computers_move(field, 'o')
    # There is only one possibility to play.
    assert result == 'oxoxoxoxoxoxoxoxoxox'


@pytest.mark.level(43)
def test_computers_move_almost_full_end():
    """turn of the computer to almost full field (free in the end)"""
    from game_ai import computers_move
    field = 'oxoxoxoxoxoxoxoxoxo-'
    result = computers_move(field, 'x')
    # There is only one possibility to play.
    assert result == 'oxoxoxoxoxoxoxoxoxox'

@pytest.mark.level(43)
def test_computers_move_almost_full_end2():
    """turn of the computer to almost full field (2times free in the end)"""
    from game_ai import computers_move
    field = 'xooxxooxoxoxoxooxx--'
    result = computers_move(field, 'x')
    assert len(result) == 20, result + ': Wrong length of field'
    assert result.count('x') == 10, result + ': Wrong number of symbols x'
    assert result.count('o') == 9, result + ': Wrong number of symbols o'


@pytest.fixture
def push_input(monkeypatch):
    """Push input to the function like users gave it."""
    # Tohle je trochu pokročilá testovací magie.
    # Viz pokročilý kurz: https://naucse.python.cz/course/mi-pyt/intro/testing/
    input = []
    def _give_input(*args):
        input.extend(args)
    def pushed_input(question):
        assert input != [], 'Program should not ask on the other question. '
        answer = input.pop(0)
        print(question + answer)
        return answer
    monkeypatch.setattr(builtins, 'input', pushed_input)
    yield _give_input
    # Kontrola, že všechno ze inputu bylo přečteno:
    assert input == [], 'Unread answers'
