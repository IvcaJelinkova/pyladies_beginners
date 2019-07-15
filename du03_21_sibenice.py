# du21_sibenice.py
# rozdel projekt do funkci a modulu s hezkymi jmény, piš testy a dokumentační řetězce,
# funkční kousky dávej postupně do Gitu.

# OK - Počítač náhodně zvolí slovo (trávník, stromek, stavení). malá písmena a bez opakujících se písmen (čokoláda).

# OK - Výchozí stav je řetězec s tolika podtržítky, kolik je ve vybraném slově písmen.
# OK - Výchozí počet neúspěšných pokusů je nula.
# Stále dokola:
    # OK - Zeptej se hráče na písmeno.
    # OK - Pokud je to písmeno ve vybraném slově, zaměň ve stavu příslušná podtržítka
            # za ono písmeno. (Bude se hodit řetězcová metoda index. a funkce zamen.)
    # OK - Pokud dané písmeno není ve vybraném slově, započítej neúspěšný pokus.
    # OK - Vypiš stav (slovo s případnými podtržítky).
    # OK - Pokud už ve slově nejsou podtržítka, pogratuluj hráči a ukonči hru.
    # OK - Vypiš počet neúspěšných pokusů a odpovídající obrázek. Funkci, která ti vrátí
    #       obrázek podle počtu pokusů, si můžeš stáhnout z Gitu
    # OK - Pokud je počet neúspěšných pokusů 9 (nebo víc), hráč prohrál. Dej mu to najevo a ukonči program.

from random import choice


def vyber_slovo():
    """Vybere slovo k hádání a nahradí písmena podtržítky. Vyresetuje neúspěšné pokusy. """
    vybrane_slovo = choice(['trávník', 'stromek', 'stavení', 'čokoláda', 'ananas'])
    hadane_slovo = len(vybrane_slovo) * '_ '
    neuspesne_pokusy = 0
    return vybrane_slovo, hadane_slovo, neuspesne_pokusy


def zamen(hadane_slovo, pozice, hadane_pismeno):
    """Zaměňuje podtržítko za hádané písmeno."""
    zacatek = hadane_slovo[ :pozice]
    prostredek = hadane_pismeno
    konec = hadane_slovo[pozice + 1: ]
    return zacatek + prostredek + konec


def mozne_vstupy():
    """Kontroluje, zda hádané písmeno je mezi možnými vstupy do tajenky. Nepřípustné jsou číslice,
    shluky písmen a jiné znaky. """
    hadane_pismeno = input('\nHádané písmeno: ')
    while True:
        if hadane_pismeno in "aábcčdďeéěfghchiíjklmnňoópqrřsštťuúůvwxyýzž" and len(hadane_pismeno) == 1:
            return hadane_pismeno
        else:
            hadane_pismeno = input("Zadávej pouze jednotlivá písmena. Hádané písmeno: ")


def obrazek(level):
    """Vykresluje obrázek na základě počtu chyb."""
    if level == 0:
        return """
	    ~~~~~~~
	    """
    elif level == 1:
        return """
	    +
	    |
	    |
	    |
	    |
	    |
	    ~~~~~~~
	    """
    elif level == 2:
        return """
	    +---.
	    |
	    |
	    |
	    |
	    |
	    ~~~~~~~
	    """
    elif level == 3:
        return """
	    +---.
	    |   |
	    |
	    |
	    |
	    |
	    ~~~~~~~
	    """
    elif level == 4:
        return """
	    +---.
	    |   |
	    |   O
	    |
	    |
	    |
	    ~~~~~~~
	    """
    elif level == 5:
        return """
	    +---.
	    |   |
	    |   O
	    |   |
	    |
	    |
	    ~~~~~~~
	    """
    elif level == 6:
        return """
	    +---.
	    |   |
	    |   O
	    | --|
	    |
	    |
	    ~~~~~~~
	    """
    elif level == 7:
        return """
	    +---.
	    |   |
	    |   O
	    | --|--
	    |
	    |
	    ~~~~~~~
	    """
    elif level == 8:
        return """
	    +---.
	    |   |
	    |   O
	    | --|--
	    |  /
	    |
	    ~~~~~~~
	    """
    else:
        return """
	    +---.
	    |   |
	    |   O
	    | --|--
	    |  / \\
	    |
	    ~~~~~~~
	    """



def pozice_pismene(vybrane_slovo, hadane_pismeno):
    """Vrací seznam výskytů pozic hádaného písmene ve vybraném slově."""
    seznam_vyskytu_pismene = []
    for znak in range(len(vybrane_slovo)):
        if vybrane_slovo[znak] == hadane_pismeno:
            seznam_vyskytu_pismene.append(znak)
    return seznam_vyskytu_pismene




print('\n\n\n' + obrazek(0))
vybrane_slovo, hadane_slovo, neuspesne_pokusy = vyber_slovo()
print(hadane_slovo)


while True:
    if '_' in hadane_slovo:
        if neuspesne_pokusy < 9:
            hadane_pismeno = mozne_vstupy()
            pocet_vyskytu = 0
            if hadane_pismeno in vybrane_slovo:
                print('Trefa! ')
                seznam_vyskytu_pismene = pozice_pismene(vybrane_slovo, hadane_pismeno)
                for vyskyt_pismene in seznam_vyskytu_pismene:
                    hadane_slovo = zamen(hadane_slovo, vyskyt_pismene * 2, hadane_pismeno)  # * 2 kvůli mezerám mezi "_", pro přehlednost
                    pocet_vyskytu += 1
                    if pocet_vyskytu == len(seznam_vyskytu_pismene):
                        print('\nAktuální hádané slovo:   ' + hadane_slovo)
            else:
                neuspesne_pokusy += 1
                level = neuspesne_pokusy
                print(obrazek(level))
                print('Počet neúspěšných pokusů: ' + str(neuspesne_pokusy))
                print('\nAktuální hádané slovo:   '+ hadane_slovo)
        else:
            print('\nProhrál jsi. Šibenice splnila účel. ')
            break
    else:
        print('\nVyhrál jsi! Gratuluji. ')
        break


