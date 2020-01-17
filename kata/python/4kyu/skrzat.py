def skrzat(base, number):
    if base == 'b':
        num = list(number)
        out = int()
        i = 0
        while len(num):
            out += int(num.pop(-1)) * ((-2) ** i)
            i += 1
        return 'From binary: {bin} is {dec}'.format(bin=number, dec=str(out))
    else:
        num = number
        out = []
        while True:
            num, remainder = divmod(num, -2)
            if remainder < 0:
                num, remainder = num + 1, remainder + 2
            out.append(str(remainder))
            if num == 0: break
        return 'From decimal: {dec} is {bin}'.format(dec=number, bin=''.join(out[::-1]))