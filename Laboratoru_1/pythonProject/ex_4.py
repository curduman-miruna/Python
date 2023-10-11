import sys


def convert(text):
    result = ""
    for char in text:
        if char.isupper():
            if not result:
                result += char.lower()
            else:
                result += "_" + char.lower()
        else:
            result += char
    return result


string_to_convert = input("Introdu string: ")
print(convert(string_to_convert))
