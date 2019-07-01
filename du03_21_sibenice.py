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
		# obrázek podle počtu pokusů, si můžeš stáhnout z Gitu
	# OK - Pokud je počet neúspěšných pokusů 9 (nebo víc), hráč prohrál. Dej mu to najevo a ukonči program.

from random import randrange

slovo = ''
pocet_neuspech_pokusu = 0
pozice_pismene = ''

def vyber_slovo(slovo): 
	"""Vybere náhodně jedno ze tří slov."""
	cislo = randrange(3)
	if cislo == 0: 
		slovo = 'náhody'
	elif cislo == 1: 
		slovo = 'lotři'
	else: 
		slovo = 'stavení'
	return slovo

hadane_slovo = vyber_slovo(slovo)
#print('Vybrané slovo je:', hadane_slovo)

slovo_uhodnute = len(hadane_slovo) * '_'
#print('Délka vybraného slova je:', len(slovo_uhodnute))
print('Hádané slovo:', slovo_uhodnute)

def zamen(slovo_uhodnute, pozice, nahrada):
	zacatek	= slovo_uhodnute[ :pozice]
	prostredek = nahrada
	konec = slovo_uhodnute[pozice+1:]
	return zacatek + prostredek + konec

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


while True: 
	if '_' in slovo_uhodnute:
		if pocet_neuspech_pokusu < 9: 	
			pismeno = input('Zadej písmeno do šibenice: ')
			if pismeno in hadane_slovo:
				pozice_pismene = hadane_slovo.index(pismeno)
				#print('Zadané písmeno je na pozici:', pozice_pismene)
				slovo_uhodnute = zamen(slovo_uhodnute, pozice_pismene, pismeno)
				print('Hádané slovo:', slovo_uhodnute)
			else: 
				print('Písmeno není ve slově! ')
				pocet_neuspech_pokusu += 1
				print('Počet neúspěšných pokusů:', pocet_neuspech_pokusu)
				level = pocet_neuspech_pokusu
				print(obrazek(level))
				print('Hádané slovo:', slovo_uhodnute)
		else: 
			print('\n Šibenice splnila svůj účel. Prohrál jsi.')
			break
	else: 
		print('\n Gratuluji k výhře! ')
		break

