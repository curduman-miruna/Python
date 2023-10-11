import sys
def cmmdc(number_1, number_2):
    while number_1 != number_2:
        if number_1 > number_2:
            number_1 = number_1 - number_2
        else:
            number_2 = number_2 - number_1
    return number_1

numbers = []
num_count = int(input("Enter the number of numbers: "))

for i in range(num_count):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

if len(numbers) == 0:
    print("No numbers were entered")
elif len(numbers) == 1:
    print("Only one number was entered")
else:
    cmmdc_numbers = cmmdc(numbers[0], numbers[1])
    for index in range(2, len(numbers)):
        cmmdc_numbers = cmmdc(cmmdc_numbers, numbers[index])
    print(f"cmmmdc = {cmmdc_numbers}")




