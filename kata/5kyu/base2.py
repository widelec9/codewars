def int_to_negabinary(number):
    out = []
    while True:
        number, remainder = divmod(number, -2)
        if remainder < 0:
            number, remainder = number + 1, remainder + 2
        out.append(str(remainder))
        if number == 0: break
    return ''.join(out[::-1])


def negabinary_to_int(number):
    number = list(number)
    out = int()
    i = 0
    while len(number):
        out += int(number.pop(-1)) * ((-2) ** i)
        i += 1
    return out