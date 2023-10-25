def set_operations(*sets):
    result = {}
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            set1 = sets[i]
            set2 = sets[j]

            result[f"{set1} | {set2}"] = set1.union(set2)
            result[f"{set1} & {set2}"] = set1.intersection(set2)
            result[f"{set1} - {set2}"] = set1.difference(set2)
            result[f"{set2} - {set1}"] = set2.difference(set1)
    return result


# Example usage:
set1 = {1, 2}
set2 = {2, 3}
set3 = {3,4}
result = set_operations(set1, set2, set3)
print(result)
