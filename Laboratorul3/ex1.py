def list_operations(a, b):
    set_a = set(a)
    set_b = set(b)
    intersection = set_a.intersection(set_b)
    union = set_a.union(set_b)
    a_difference = set_a.difference(set_b)
    b_difference = set_b.difference(set_a)

    result = [intersection, union, list(a_difference), list(b_difference)]
    return result

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
result = list_operations(a, b)
print(result)
