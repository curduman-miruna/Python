def fibonacci(n):
    fibonacci_n = [0, 1]

    while len(fibonacci_n) < n:
        next_number = fibonacci_n[-1] + fibonacci_n[-2]
        fibonacci_n.append(next_number)

    return fibonacci_n[:n]

n = 10
fibonacci_list = fibonacci(n)
print(fibonacci_list)
