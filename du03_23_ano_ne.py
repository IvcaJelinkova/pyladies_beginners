# du23_ano_ne.py


def ano_ne(otazka):
    """Zeptá se na otázku. Vrátí True nebo False podle odpovědi ano/ne."""
    while True:
        odpoved = input(otazka).lower().strip()
        if odpoved in ("ano", "a"):
            return True
        elif odpoved in ("ne", "n"):
            return False
        else:
            print('Nerozumím. Zadej "ano" nebo "ne".')  # nevyskočím z cyklu a zeptám se znovu

if ano_ne('Chceš si zahrát hru?: '):
    print('OK, ale nejdřív si ji naprogramuj. :-)')
else:
    print('Škoda. ')

