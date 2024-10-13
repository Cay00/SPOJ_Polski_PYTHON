import math


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


test = int(input())

for _ in range(test):
    a = int(input())
    if is_prime(a):
        print("TAK")
    else:
        print("NIE")
