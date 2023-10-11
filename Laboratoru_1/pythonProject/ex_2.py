import sys
def check_if_vowel(char_to_check):
    vowels = "aeiouăîâAEIOUĂÎÂ"
    return char_to_check in vowels

n = input("Introdu string: ")
count = 0

for index in range(len(n)):
   if check_if_vowel(n[index]):
       count += 1

print(count)