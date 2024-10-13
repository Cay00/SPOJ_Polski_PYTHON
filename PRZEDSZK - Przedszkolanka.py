def NWD(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


proby = int(input())

for i in range(proby):
    a, b = map(int, input().split())
    wynik = a // NWD(a, b) * b
    print(wynik)
