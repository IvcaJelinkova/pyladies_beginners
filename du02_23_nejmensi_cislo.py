# du23_nejmensi.py

# Napiš program, který se pětkrát zeptá na číslo a nejmenší zadané číslo vypíše.
# Upgrade: kontroluje, zda je to číslo. Zadaná čísla vypíše v seznamu.

def zadej_cislo():
    while True:
        cislo = input('Zadej celé číslo: ')
        try:
            return int(cislo)
        except ValueError:
            print('Toto není celé číslo! ')


cislo = zadej_cislo()
seznam = []
seznam.append(cislo)
cislo_mensi = cislo
for i in range(4):
    cislo = zadej_cislo()
    seznam.append(cislo)
    if cislo < cislo_mensi:
        cislo_mensi = cislo

print(seznam)
print('Nejmenší se zadaných čísel je: ' + str(cislo_mensi) + '. ')
