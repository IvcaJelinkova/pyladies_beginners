deck_of_cards = []
numerical_values = list(range(2, 11))
letter_values = list('JQKA')

for color in '♠', '♥', '♦', '♣':
    for value in numerical_values + letter_values:
        deck_of_cards.append(str(value) + color)
print(deck_of_cards)
print(len(deck_of_cards))

seznam_seznamu = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
prvni_prvek_druheho_seznamu = seznam_seznamu[1][0]
print(prvni_prvek_druheho_seznamu)      # 4



# tabulka male nasobilky
def vytvor_radek_tabulky(cislo_radku, velikost):
    """Vrátí seznam – daný řádek tabulky s násobilkou"""
    radek = []
    for cislo_sloupce in range(velikost):
        radek.append(cislo_radku * cislo_sloupce)
    return radek

def vytvor_tabulku(velikost):
    """Vrátí seznam seznamů – tabulku s násobilkou"""
    seznam_radku = []
    for cislo_radku in range(velikost):
        radek = vytvor_radek_tabulky(cislo_radku, velikost)
        seznam_radku.append(radek)
    return seznam_radku

nasobilka = vytvor_tabulku(11)

print(nasobilka[2][3])  # dva krát tři
print(nasobilka[5][2])  # pět krát dva
print(nasobilka[8][7])  # osm krát sedm

# Vypsání celé tabulky
for radek in nasobilka:
    for cislo in radek:
        print(cislo, end=' ')
    print()


