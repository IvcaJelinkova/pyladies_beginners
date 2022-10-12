# content: 
""" 1) is this string in another string?
    2) are you male or female by last name
    3) count a letter in text
    4) 'a' 4times under itself
    
    5)      Line 0
            Line 1
            Line 2
            Line 3
            Line 4
    6)        
        0 squared is 0
        1 squared is 1
        2 squared is 4
        3 squared id 9
        4 squared id 16
    7) 
        X X X X X 
        X X X X X
        X X X X X 
        X X X X X
        X X X X X 

    8) small multiplication table:
        0       0       0       0       0
        0       1       2       3       4
        0       2       4       6       8
        0       3       6       9       12
        0       4       8       12      16

    9) print: 
        X
        X X
        X X X
        X X X X

    10) print: 
        first line
        not first
        not first
        not first

    11) print: 
        X X X X X X
        X         X
        X         X
        X         X
        X         X
        X X X X X X
    """

""" 
# ad1) is this string in another string? 
string1 = input('Enter a string to know, if it\'s in the next string: ').lower()
string2 = input('Enter the second string: ').lower()
if string1 in string2: 
    print('Yes, the first string is in the second. \n')
elif string2 in string1: 
    print('Yes, the second string is in the first. \n')
else: 
    print('No, the first string is not in the second or conversely. \n')


# ad2) are you male or female by last name: 
surname = input('Enter your surname: ').lower()

if surname[-1:] in ('a', 'á'): 
    print('You are female. \n')
else: 
    print('You are male. \n')
""" 

# ad3) count a letter in text: 
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


""" 
# ad4) 'a' 4times under itself: 
for i in range(4): 
    print('a')

print()
""" 

# ad5) print:    
"""         Line 0
            Line 1
            Line 2
            Line 3
            Line 4""" 

for number_of_line in range(5): 
    print(f'Line {number_of_line}')

print()



# ad6) print: 
""" 0 squared is 0
    1 squared is 1
    2 squared is 4
    3 squared id 9
    4 squared id 16"""

for number_of_line in range(5): 
    print(f'{number_of_line} squared is {number_of_line ** 2}')

print()

# ad7) print: 
""" X X X X X 
    X X X X X
    X X X X X 
    X X X X X
    X X X X X 
condition: every print print only one 'X' """

for number_of_line in range(5): 
    for number_of_char in range(5): 
        print('X ', end='')
    print()


print()

# ad8) print small multiplication table: 
""" 0       0       0       0       0
    0       1       2       3       4
    0       2       4       6       8
    0       3       6       9       12
    0       4       8       12      16
""" 

for number_of_line in range(5): 
    for number_of_char in range(5): 
        print(number_of_line * number_of_char, end='\t')
    print()

print()


# ad9) print: 
""" X
    X X
    X X X
    X X X X"""

for number_of_line in range(4): 
    for number_of_char in range(4): 
        if number_of_line >= number_of_char:
            print('X', end=' ')
    print()

print()


# ad10) print: 
"""     first line
        not first
        not first
        not first""" 

for number_of_line in range(4): 
    if number_of_line == 0: 
        print('first line')
    else: 
        print('not first')

print()


# ad11) print: (print must contain only one 'x')
"""     X X X X X X
        X         X
        X         X
        X         X
        X         X
        X X X X X X """ 

for number_of_line in range(6): 
    for number_of_char in range(6): 
        if number_of_line in (0, 5) or number_of_char in (0, 5): 
            print('X', end=' ')
        else: 
            print(' ', end=' ')
    print()



