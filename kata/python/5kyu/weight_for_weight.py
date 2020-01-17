def order_weight(strng):
    return ' '.join([k[1] for k in sorted([(sum(map(int, v)), v) for v in strng.split(' ')])])
