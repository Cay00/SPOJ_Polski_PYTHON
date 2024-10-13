test = int(input())


def factorial_last(n):
    if n >= 10:
        return (0, 0)
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        ones = factorial % 10
        tens = int((factorial % 100 - ones) / 10)
        return (tens, ones)


for _ in range(test):
    n = int(input())
    tens, ones = factorial_last(n)
    print(tens, ones)
