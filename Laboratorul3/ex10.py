def loop(route):
    #route = dictionar pentru fiecare valoare
    visited = set()
    result = []
    current_key = "start"
    #cat timp cheia e in dictionar si nu a fost vizitata pentru a evita loopurile
    while current_key in route and current_key not in visited:
        result.append(route[current_key])
        visited.add(current_key)
        current_key = route[current_key]

    return result


mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
result = loop(mapping)
print(result)
