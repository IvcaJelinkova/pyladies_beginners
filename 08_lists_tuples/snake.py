#game snake.py

#make this: 
""" 
X X X X X
X X X X X
X X X X X
X X X X X
X X X X X
"""

for raw in range(5): 
    for collumn in range(5):
        print('X', end=' ')
    print() 
print()


#make a table with small multiplication: 
""" 
0 0 0 0 0
0 1 2 3 4
0 2 4 6 8
0 3 6 9 12
0 4 8 12 16
"""

for raw in range(5): 
    for collumn in range(5): 
        print(collumn * raw, end=' ')
    print()
print()


# make this: 
""" 
X . . . . . . . . .
X . . . . . . . . .
. . X . . . . . . .
. . . . . . . . . .
. . . X . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . X
. . . . . . . . . .
"""

def make_map(coordinates): 
    """Gets list of coordinates and returns map like grid 10×10. On the field in list print 'X', elsewhere '.'.
    'coordinates' are pair of numbers smaller than 10, which determine collumn and raw. """
    table = []
    for raw in range(10): 
        for collumn in range(10): 
            raw_collumn = raw, collumn
            if raw_collumn in coordinates: 
                print('X', end=' ')
            else: 
                print('.', end=' ')
            #print(table, end=' ')
            
            #print('.', end=' ')
        print()
    print()
    return 

print(make_map([(0, 0), (1, 0), (2, 2), (4, 3), (8, 9), (8, 9)]))


# remembering a table!!! 
def make_raw(number_of_raw, size): 
    """Creates a raw (like a list) according to given number_of_raw and size. """
    raw = []
    for number_of_collumn in range(size): 
        raw_collumn = number_of_raw, number_of_collumn
        raw.append(raw_collumn)
    return raw

def make_table(size): 
    """Creates a list of lists with raws. """
    list_of_raws = []
    for number_of_raw in range(size): 
        raw = make_raw(number_of_raw, size)
        list_of_raws.append(raw)
    return list_of_raws

table = make_table(10)
print(table)

