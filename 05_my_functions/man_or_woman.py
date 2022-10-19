def man_or_woman(question): 
    """Returns sex according to given surname. """
    surname = input(question)
    if surname[-1] == 'á': 
        return 'woman'
    return 'man'

print(man_or_woman('What surname you want to test? '))