# Ex 6
def is_palindrome_number(number):
    number_str = str(number)
    return number_str == number_str[::-1]


print(is_palindrome_number(121))


# Ex 7.
def check_if_number(char_to_check):
    numbers = "0123456789"
    return char_to_check in numbers


def extract_number(text):
    number = 0
    count = 0
    for char in text:
        if check_if_number(char):
            number = number * 10 + int(char)
            count += 1
        else:
            if count > 0:
                return number
    if count == 0:
        return None
    else:
        return number


print(extract_number("vjg765hhh123fmjfdh6544snkjdg"))

# Ex. 8
def count_bits(number):
    bin_number = bin(number)
    count = bin_number.count('1')
    return count


print(count_bits(2))

# Ex. 9

def most_common_char(text):
    text = text.lower()
    letter_counts = {}
    for char in text:
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    most_common = max(letter_counts, key=letter_counts.get)
    return f"The most common character is '{most_common}' ({letter_counts[most_common]} times)."


print(most_common_char("An apple is not a tomato"))

# Ex. 10

def count_words(text):
    words = text.split(" ")
    count = 0
    for word in words:
        if word:
            count+=1
    return count

word_count = count_words("I have Python exam")
print(f"The text has {word_count} words.")