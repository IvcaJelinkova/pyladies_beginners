# is this string in another string? 
string1 = input('Enter a string to know, if it\'s in the next string: ').lower()
string2 = input('Enter the second string: ').lower()
if string1 in string2: 
    print('Yes, the first string is in the second. \n')
elif string2 in string1: 
    print('Yes, the second string is in the first. \n')
else: 
    print('No, the first string is not in the second or conversely. \n')


# are you male or female by last name: 
surname = input('Enter your surname: ').lower()

if surname[-3:] in ('ová', 'ova'): 
    print('You are female. \n')
else: 
    print('You are male. \n')


# count a letter in text: 
text = """Léta tam stál, stojí tam dál
pivovar u cesty, každý ho znal
léta tam stál, stát bude dál
ten kdo zná Jarošov, zná pivovar.Bíla pěna, láhev orosená
chmelový nektar já znám
jen jsem to zkusil a jednou se napil
od těch dob žízeň mám.Bída a hlad, kolem šel strach
když bylo piva dost, mohl ses smát
třista let stál, stát bude dál
ten kdo zná Jarošov zná pivovar.""".lower()

letter = 'a'
count = text.count(letter)
print(f'Count of a letter {letter} in your text: ', count, '\n')



# 'a' 4times under itself: 
for i in range(4): 
    print('a')

print()


# print:    Line 0
"""         Line 1
            Line 2
            Line 3
            Line 4""" 

for number_of_line in range(5): 
    print(f'Line {number_of_line}')

print()



# print: 
""" 0 squared is 0
    1 squared is 1
    2 squared is 4
    3 squared id 9
    4 squared id 16"""
