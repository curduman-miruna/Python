def order(tuples):
    def sorting_key(tuple_item):
        second_element = tuple_item[1]
        if len(second_element) >= 3:
            return second_element[2]
        else:
            return None

    sorted_tuples = sorted(tuples, key=sorting_key)
    return sorted_tuples

tuples = [('abc', 'bcd'), ('abc', 'zza')]
sorted_tuples = order(tuples)
print(sorted_tuples)
