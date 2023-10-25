def count_elements(input_list):
    set1 = set(input_list)
    #un set nu contine duplicate
    unique_elem = len(set1)
    duplicate_elem = len(input_list) - unique_elem
    return (unique_elem, duplicate_elem)

my_list = [1, 2, 2, 3, 4, 4, 5]
result = count_elements(my_list)
print(result)