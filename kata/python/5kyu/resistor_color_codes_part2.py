def encode_resistor_colors(r):
    code = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'gray', 'white']
    r = float(r[:-6]) * 1e6 if 'M' in r else float(r[:-6]) * 1e3 if 'k' in r else float(r[:-5])
    return '{} {} {} {}'.format(code[int(str(r)[0])], code[int(str(r)[1])], code[str(r)[2:-2].count('0')], 'gold')
