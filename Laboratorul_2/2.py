import math
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def prime_numbers(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
prime_list = prime_numbers(numbers)
print(prime_list)
