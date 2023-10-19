def find(numbers):
    count = 0
    max = None

    for num in numbers:
        if str(num) == str(num)[::-1]:
            count += 1
            if max is None or num > max:
                max = num

    return (count, max)

# Example usage:
numbers = [121, 123, 1331, 1001, 456, 7887, 232]

count, max = find(numbers)
print("Nr: ", count)
print("Max:", max)
