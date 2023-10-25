def counting(*args, **kwargs):
    #*args - 1 2 3 4
    #**kwargs dictionarul x=1 etc.
    matching_count = 0
    for arg in args:
        if arg in kwargs.values():
            matching_count += 1

    return matching_count

result = counting(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(result)
