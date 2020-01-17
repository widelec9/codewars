def expanded_form(num):
    num_arr = []
    div = 10
    while num > 0:
        rem = num % div
        num_arr += [int(rem)]
        num -= int(div * (rem/div))
        div *= 10
    return ''.join([str(n) + ' + ' for n in sorted(num_arr, reverse=True) if n != 0])[:-3]