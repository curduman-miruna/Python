def compare_dicts(dict1, dict2):
    if sorted(dict1.keys()) != sorted(dict2.keys()):
    #verificam daca cheile dictionarului sunt aceleasi desi ar fi permutari
        return False

    for key in dict1:
        value1 = dict1[key]
        value2 = dict2[key]
        #valorile asociate cheilor din fiecare dictionar
        if type(value1) != type(value2):
            return False

        #1. daca sutn dictionare
        if isinstance(value1, dict):
            if not compare_dicts(value1, value2):
                return False

        #2. daca sunt liste sau multimi
        elif isinstance(value1, (list, set)):
            if sorted(value1) != sorted(value2):
                return False

        #3. daca sunt doar valori
        else:
            if value1 != value2:
                return False

    return True

dict1 = {
    'a': 1,
    'b': [2, 3],
    'c': {
        'x': 'apple',
        'y': [4, 5]
    }
}

dict2 = {
    'b': [3, 2],
    'a': 1,
    'c': {
        'y': [5, 4],
        'x': 'apple'
    }
}

result = compare_dicts(dict1, dict2)
print(result)
