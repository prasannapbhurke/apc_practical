def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def sum_of_digits(n):
    n = abs(n)
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

def to_binary(n):
    if n < 0:
        return "-" + to_binary(-n)
    if n <= 1:
        return str(n)
    return to_binary(n // 2) + str(n % 2)
