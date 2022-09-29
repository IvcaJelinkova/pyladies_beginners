#testy.py spouštím python3 -m pytest -v testy.py

from examples import obvod, obsah

def test_obvod_ctverce_o_strane_2_je_8(): 
    assert obvod(2) == 8
