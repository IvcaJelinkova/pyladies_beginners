# 1D piškvorky

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

print('Stav hry je: ' + vyhodnot('jsijdsiodjo'))


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
        konec = pole[pozice+1:]
        
        #print(pole[pozice])
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
    while True:
        pozice = input('Na jakou pozici chceš hrát? (Zadej číslo 0–19.) ')
        try:
            pozice = int(pozice)
            #if (pozice < 0) or (pozice > 19):      # toto je super, ale mám to tu 2x!!
            #    print('Zadej číslo od 0 do 19! ')
            #    pass
            print("došlo to sem")
            # vychytat chyby a zeptat se znovu na pozici
            try:
                pole = tah(pole, pozice, symbol)
                print("jsem tu")
                return pole
            except ValueError:
                print("Nadávám ti! Nauč se hrát! :-)")

        except ValueError:
            print('Zadej číslo! ')


print(tah_hrace('--------------------','x'))


# 4)

