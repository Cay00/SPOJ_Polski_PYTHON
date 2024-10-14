def lustrzane_odbicie(num_dec):
    num_bin = bin(num_dec)[2:]  # Konwersja liczby dziesiętnej na binarną
    num_bin_2 = num_bin[::-1]    # Odwrócenie binarnej reprezentacji
    num_dec_2 = int(num_bin_2, 2)  # Konwersja odwróconej binarnej na dziesiętną
    return num_dec_2

data = []
while True:
    input_data = input()
    if input_data == "":  # Przerywamy wczytywanie, gdy użytkownik poda pusty ciąg
        break
    try:
        number = int(input_data)  # Próbujemy zamienić wejście na liczbę całkowitą
        data.append(number)        # Dodajemy liczbę do listy
    except ValueError:
        break

for number in data:
    output = lustrzane_odbicie(number)
    print(output)
