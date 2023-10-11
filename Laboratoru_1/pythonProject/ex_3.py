import sys


def count_occurrences(sub_string, main_string):
    count = 0
    while sub_string in main_string:
        count += 1
        index = main_string.find(sub_string)  # Find the first occurrence
        main_string = main_string[:index] + main_string[index + len(sub_string):]  # Cut the main_string

    return count

string_1 = input("Introdu substring: ")
string_2 = input("Introdu mainstring: ")
print(count_occurrences(string_1,string_2))
