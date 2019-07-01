# 1) Pomocí cyklu for napiš program, který vypíše:
#
# 0 na druhou je 0
# 1 na druhou je 1
# 2 na druhou je 4
# 3 na druhou je 9
# 4 na druhou je 16

# 1.1) Počet řádků zadává uživatel:
print('1. úkol: ')

pocet_radku = int(input('Zadej počet řádků: '))

for cislo_radku in range (pocet_radku):
    druha_mocnina = cislo_radku ** 2
    print(str(cislo_radku) + ' na druhou je ' + str(druha_mocnina))


# 2) Pomocí cyklů for + parametru end pro print napiš program, který postupně z jednotlivých 'X' vypíše:
#
# X X X X X
# X X X X X
# X X X X X
# X X X X X
# X X X X X
# počet řádků zadává uživatel:
# nepoužívej print('X X X ...')
print('\n2. úkol: ')

znak = input('Zadej opakující se znak: ')
pocet_radku = int(input('Zadej počet řádků: '))

for cislo_radku in range(pocet_radku):
    print((znak + ' ') * pocet_radku, end='\n')


# 3) Napiš program, který vypíše „tabulku“ s násobilkou.
#
# 0 0 0 0 0
# 0 1 2 3 4
# 0 2 4 6 8
# 0 3 6 9 12
# 0 4 8 12 16

print('\n3. úkol: ')

pocet_radku = int(input('Zadej počet čísel, pro které chceš násobilku (činitel 1): '))
pocet_sloupcu = int(input('Zadej počet čísel – kolikrát chceš číslo násobit (činitel 2): '))

for cislo_radku in range(pocet_radku):
    for cislo_sloupce in range(pocet_sloupcu):
        print(cislo_radku * cislo_sloupce, end=' ')
    print()


# 4) Napiš program, který postupně z jednotlivých 'X' vypíše:
#
# X
# X X
# X X X
# X X X X
# znak si zadá uživatel
# počet řádků si zadá uživatel

print('\n4. úkol: ')

znak = input('Jaký znak chceš opakovat? ')
pocet_radku = int(input('Zadej počet řádků: '))

for cislo_radku in range(pocet_radku):
    print((znak + ' ') * (cislo_radku + 1))


# 5) Pomocí cyklu for a příkazu if napiš program, který vypíše následující řádky. Funkci print volej pouze uvnitř v cyklu:
#
# první řádek
# není první
# není první
# není první

print('\n5. úkol: ')

pocet_radku = int(input('Zadej počet řádků: '))
for cislo_radku in range(pocet_radku):
    if cislo_radku == 0:
        print('první řádek')
    else:
        print('není první')


# 6) Pomocí cyklů for a příkazu if napiš program, který z jednotlivých 'X' a mezer vypíše:
#
# X X X X X X
# X         X
# X         X
# X         X
# X         X
# X X X X X X
# znak a počet řádků uživatel zadá

print('\n6. úkol: ')

znak = input('Zadej znak: ')
pocet_radku = int(input('Zadej počet řádků: '))
pocet_sloupcu = int(input('Zadej počet sloupců: '))
for cislo_radku in range(pocet_radku):
    if cislo_radku in (0, pocet_radku - 1):
        print((znak + ' ') * pocet_sloupcu)
    else:
        print(znak + ' ' + (' ' * 2) * (pocet_sloupcu - 2) + znak)
