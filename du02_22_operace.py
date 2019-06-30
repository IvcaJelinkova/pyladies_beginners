# du22_operace.py
# Napiš program, který postupně načte od uživatele dvě čísla a jednoznakový řetězec – buď '+', '-', '*' nebo '/'.
# Program provede na číslech příslušnou operaci.

print('Tento program po zadání dvou čísel provede vámi zadanou operaci (+, -, *, /). ')
prvni_cislo = int(input('Zadej první číslo: '))
druhe_cislo = int(input('Zadej druhé číslo: '))
operace = input('Operace: ')
vysledek = 0

if operace == '+':
    vysledek = prvni_cislo + druhe_cislo
elif operace == '-':
    vysledek = prvni_cislo - druhe_cislo
elif operace == '*':
    vysledek = prvni_cislo * druhe_cislo
elif operace == '/':
    if druhe_cislo == 0:
        print('Dělení nulou nelze. ')
    else:
        vysledek = prvni_cislo % druhe_cislo
else:
    print('Zadej +, -, * nebo /. ')

print(str(prvni_cislo) + ' ' + operace + ' ' + str(druhe_cislo) + ' ' + '=' + ' ' + str(vysledek))


