def make_list_of_animals(): 
    "Creates new list of animals and will return it." 
    animals = []
    for animal in "dog", "cat", "rabbit", "snake": 
        animals.append(animal)
    return animals

# print(make_list_of_animals())
animals = make_list_of_animals()
# print(animals.pop())
# print(animals)
# print(make_list_of_animals())



def filter_short_names(animals): 
    """Gets list of strings, returns list of those which are shorther than 5 characters. """
    short_names = []
    for animal in animals: 
        if len(animal) < 5: 
            short_names.append(animal)
    return short_names

print(filter_short_names(animals))



def filter_c(animals): 
    """Gets a list of strings, returns list of those which starts on 'k'. """
    starts_on_c = []
    for animal in animals: 
        if animal[0] == 'c': 
            starts_on_c.append(animal)
    return starts_on_c

print(filter_c(animals))



def contains(list, word): 
    """Gets a list and a word and checks if the word is in the list --> than returns True, False otherwise. """
    if word in list: 
        return True
    else: 
        return False

print(contains(animals, 'cat'))



def without_the_first(list): 
    """Gets a list of names and returns the list with all of elements without the first. """
    return list[1:]

print(animals)
print(without_the_first(animals))



def sort_from_the_second_letter(list): 
    """Gets a list of words and returns the list sorted according to the second letter of every word. """
    helped_list = []
    sorted_list_animals = []
    for word in list: 
        character_word = word[1:], word
        helped_list.append(character_word)
    sorted_list = sorted(helped_list)
    for i in range(len(sorted_list)): 
        sorted_list_animals.append(sorted_list[i][1])
    return sorted_list_animals

zvirata = ["králík", "andulka", "pes", "kočka", "had"]
print(zvirata)
print(sort_from_the_second_letter(zvirata))



