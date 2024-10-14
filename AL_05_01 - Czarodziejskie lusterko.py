while True:
    try:
        data_in = input()
        if data_in == "":
            break
        number_dec = int(data_in)
        number_bin = bin(number_dec)[2:]
        number_dec_2 = number_bin[::-1]
        number_bin_2 = int(number_dec_2, 2)

        print(number_bin_2)

    except ValueError:
        break
