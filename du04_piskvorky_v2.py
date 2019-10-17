# 1D piškvorky

from random import randrange


# řádek: 20 políček, vítěz: 3 symboly stejné

# 1)
# Napiš funkci vyhodnot, která dostane řetězec s herním polem 1-D piškvorek a vrátí jednoznakový řetězec podle stavu hry:

# "x" – Vyhrál hráč s křížky (pole obsahuje "xxx")
# "o" – Vyhrál hráč s kolečky (pole obsahuje "ooo")
# "!" – Remíza (pole neobsahuje "-", a nikdo nevyhrál)
# "-" – Ani jedna ze situací výše (t.j. hra ještě neskončila)

def vyhodnot(pole):
    if 'xxx' in pole:
        stav_hry = 'x'
    elif 'ooo' in pole:
        stav_hry = 'o'
    elif '-' not in pole:
        stav_hry = "!"
    else:
        stav_hry = '-'

    return stav_hry

#print('Stav hry je: ' + vyhodnot('jsijdsiodjo'))


# 2)
# Napiš funkci tah, která dostane řetězec s herním polem, číslo políčka (0-19), a symbol (x nebo o) a vrátí herní pole (t.j. řetězec)
# s daným symbolem umístěným na danou pozici.

# Přepiš funkci tah, aby skončila s chybou ValueError v těchto případech:

# Hra na pozici, která není v poli, např. tah('--------------------', -1, 'x')
# Hra na obsazené políčko, např. tah('x-------------------', 0, 'o')
# Hra jiným symbolem než 'x' nebo 'o', např. tah('--------------------', 0, 'řeřicha')



def tah(pole, pozice, symbol):
    """Vrátí herní pole se symbolem umístěným na pozici

    'pole' je pole, na které se hraje
    'pozice' je číslo políčka (0–19)
    'symbol' je 'x' nebo 'o' podle toho, za co se hraje
    Skončí ValueError, pokud se hraje mimo pole, pokud je políčko obsazené, chceme hrát jiným symbolem. """

    if ((pozice < 0) or (pozice > 19) or (pole[pozice] != '-') or (symbol not in ('x', 'o'))):
        raise ValueError("Pozice může být pouze 0–19, na pozici musí být '-', hrát se smí pouze 'x' nebo 'o'.")
    else:
        zacatek = pole[0:pozice]
        konec = pole[pozice + 1:]
        pole = zacatek + symbol + konec

        return pole

#tah('----o', 4, 'cha')



# 3)
# Napiš funkci tah_hrace(pole, symbol), která dostane řetězec s herním polem a symbol (x nebo o) a:

# dostane řetězec s herním polem,
# zeptá se hráče, na kterou pozici chce hrát,
# pomocí funkce tah zjistí, jak vypadá herní pole se zaznamenaným tahem hráče
# OK vrátí toto herní pole se zaznamenaným tahem hráče.
# OK Pokud uživatel zadá špatný vstup (nečíslo, záporné číslo, obsazené políčko apod.), funkce mu vynadá a zeptá se znova.

def tah_hrace(pole, symbol):
    """Dostane řetězec s herním polem a symbol. """
    while True:
        pozice = input('Na jakou pozici chceš hrát? (Zadej číslo 0–19.) ')
        try:
            pozice = int(pozice)

            # vychytat chyby a zeptat se znovu na pozici
            try:
                pole = tah(pole, pozice, symbol)
                return pole
            except ValueError:
                print("Nadávám ti! Nauč se hrát! :-)")

        except ValueError:
            print('Zadej číslo! ')

#print(tah_hrace('--------------------','x'))


# 4) Napiš funkci tah_pocitace(pole, symbol), která dostane řetězec s herním polem a symbol, vybere pozici, na kterou hrát, a vrátí herní pole se
# zaznamenaným tahem počítače.
#
# Použij jednoduchou náhodnou „strategii”:
#
# OK Vyber číslo od 0 do 19.
# OK Pokud je dané políčko volné, hrej na něj.
# OK Pokud ne, opakuj od bodu 1.

def tah_pocitace(pole, symbol):
    """Vrátí herní pole se zaznamenaným tahem počítače

    `pole` je herní pole, na které se hraje.
    `symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky nebo za kolečka."""
    if '-' not in pole:
        return print('Není kam hrát! ')
    while True:
        pozice = randrange(0, 20)
        if pole[pozice] == '-':
            pole = tah(pole, pozice, symbol)
            return pole

#print(tah_pocitace('xxxxxxxxxx--xxxxxxxx', 'o'))



# 5) Napiš funkci piskvorky1d, která:
#
# Vytvoří řetězec s herním polem
# Stále dokola:
# zavolá volá funkci tah_hrace, a výsledek uloží jako nové pole
# vypíše stav hry
# zavolá volá funkci tah_pocitace, a výsledek uloží jako nové pole
# vypíše stav hry
# Zatím neřeš konec hry.


# 6) Teď pošéfuj konec hry. Když někdo vyhraje nebo dojde k remíze, cyklus se ukončí a vypíše se výsledek – třeba s gratulací nebo povzbuzující zpráva.
# Stav hry kontroluj po každém tahu.



def piskvorky1d(symbol, symbol_pc):
    """Vytvoří řetězec s herním polem, volá funkci tah_hrace, uloží nové pole, vypíše stav hry.
    Volá funkci tah_pocitace, uloží nové pole, vypíše stav hry."""
    pole = 20 * '-'

    while '-' in pole:
        pole = tah_hrace(pole, symbol)
        print('Herní pole po tahu hráče je: ' + pole)
        if vyhodnot(pole) == symbol:
            return print('Vyhrál jsi. Gratuluji. :-) ')
        elif vyhodnot(pole) == '!':
            return print('Remíza. ')

        pole = tah_pocitace(pole, symbol_pc)
        print('Herní pole po tahu PC je: ' + pole)
        if vyhodnot(pole) == symbol_pc:
            return print('Vyhrál počítač. Hodně štěstí příště. :-) ')
        elif vyhodnot(pole) == '!':
            return print('Remíza. ')

    return print('Není kam hrát! ')



symbol = input('Chceš hrát za "x" nebo za "o"? ')
while symbol not in ('x', 'o'):
    symbol = input('Chceš hrát za "x" nebo za "o"? ')

if symbol == 'x':
    print('Hraješ za "x". ')
    symbol_pc = 'o'
else:
    print('Hraješ za "o". ')
    symbol_pc = 'x'



piskvorky1d(symbol, symbol_pc)





