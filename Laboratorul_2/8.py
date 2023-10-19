def search(x=1, strings=[], flag=True):
    characters = []
    for string in strings:
        char_list = []
        for char in string:
            if (ord(char) % x == 0) if flag else (ord(char) % x != 0): #ord - unicode al unei character
                char_list.append(char)
        characters.append(char_list)
    return tuple(characters)

x = 2
strings = ["test", "hello", "lab002"]
flag = False

list = search(x, strings, flag)
print(list)
