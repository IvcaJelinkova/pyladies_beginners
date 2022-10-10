def smallest(number, the_smallest): 
    """App pick the smallest number from five numbers. """
    if number < the_smallest: 
        the_smallest = number
        print('jsem tu')
        return the_smallest
    return the_smallest
    

for i in range(1, 6):
    number = int(input(f'Enter {i}. number: '))
    if i == 1: 
        the_smallest = number
    the_smallest = smallest(number, the_smallest)
    #print('nejmenší: ', the_smallest)
print('The smallest number is:', the_smallest)
