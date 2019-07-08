# du25_kostka.py
# Prvni hrac hazi kostkou (t.j. vybiraji se nahodna cisla od 1 do 6), dokud nepadne sestka. Potom hazi dalsi hrac,
# dokud nepadne sestka i jemu. Potom hazi hrac treti a nakonec ctvrty.
# OK – Vyhrava ten, kdo na hozeni sestky potreboval nejvic hodu. (V pripade shody vyhraje ten, kdo hazel driv.)
#
# OK – Program by mel vypisovat vsechny hody a nakonec napsat, kdo vyhral.
#
# OK – Napoveda: prubezne staci ukladat jen udaj, kdo vede.

from random import randrange

vitezny_pocet_pokusu = 0

for poradi_hrace in range(1, 5):
    pocet_pokusu = 0
    print(f'\n\n Hází {poradi_hrace}. hráč. ')
    while True:
        prvni_hrac = randrange(0, 7)
        if prvni_hrac == 6:
            pocet_pokusu = pocet_pokusu + 1
            print('Padla Ti šestka. Gratuluji. Konečný počet pokusů: ' + str(pocet_pokusu) + '. ')
            if pocet_pokusu > vitezny_pocet_pokusu:
                vitezny_pocet_pokusu = pocet_pokusu
                vitez = poradi_hrace

            break
        else:
            pocet_pokusu = pocet_pokusu + 1
            print('Nepadla Ti šestka, házíš dál. Počet pokusů: ' + str(pocet_pokusu))
print('Vítěz je hráč č.: ' + str(vitez) + '. Obrovská gratulace, jdi to zapít! :-)')

