# oko bere
# Začínáš se skóre 0 bodů.
'''
V každém kole:
	Počítač vypíše, kolik máš bodů.
	Počítač se zeptá, jestli chceš pokračovat.
	Pokud byla odpověď „ne“:
		Hra končí.
	Jinak:
		Počítač „vybere kartu“ – náhodně vybere číslo od 2 do 10;
		vybranou hodnotu vypíše;
		přičte tuto hodnotu ke skóre.
	Pokud máš víc než 21 bodů:
		Počítač vypíše, že prohráváš;
		hra končí.
Po skončení hry počítač vypíše dosažené skóre.
Cílem hry je neprohrát a získat přitom co nejvíc bodů, ideálně 21.
'''

from random import randrange

skore = 0
print('Tvé skóre je: ' + str(skore) + '. ')

while skore <= 21:
	odpoved = input('Chceš pokračovat? ')

	if odpoved == 'ne' or odpoved == 'Ne':
		print('Konec hry. ')
		break
	elif odpoved == 'ano' or odpoved == 'Ano': 
		karta = randrange(2, 11)
		print('Hodnota vylosované karty je: ' + str(karta) + '. ')
		skore = skore + karta
		print('Tvé skóre je: ' + str(skore) + '. ')
	else: 
		print('Zadej ano nebo ne. ')
if skore > 21:
	print('Prohráváš.')
print('Tvé konečné skóre je: ' + str(skore) + '. ')