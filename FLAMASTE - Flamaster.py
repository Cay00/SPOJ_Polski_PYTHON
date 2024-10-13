test = int(input())

for _ in range(test):
    input_data = input()
    counter = 1

    for i in range(1, len(input_data) + 1):
        if i == len(input_data) or input_data[i] != input_data[i - 1]:
            if counter > 2:
                print(input_data[i - 1], counter, sep='', end='')
            elif counter == 2:
                print(input_data[i - 1] * 2, end='')
            else:
                print(input_data[i - 1], end='')
            counter = 1
        else:
            counter += 1

    print()
