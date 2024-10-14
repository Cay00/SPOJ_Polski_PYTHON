t = int(input())

for _ in range(t):
    n = int(input())
    liczby = list(map(int, input().split()))

    print(sum(liczby))
