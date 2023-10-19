def list_operations(a, b):
    intersection = list(set(a) & set(b))
    union = list(set(a) | set(b))
    a_b = list(set(a) - set(b))
    b_a = list(set(b) - set(a))

    return intersection, union, a_b, b_a


list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

intersection, union, a_b, b_a = list_operations(list_a, list_b)
print("Intersectie = ", intersection)
print("Reuniunea = ", union)
print("A - B = ", a_b)
print("B - A = ", b_a)
