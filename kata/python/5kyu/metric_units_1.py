def meters(x):
    x = int(x)
    if x < 1000:
        return str(x) + 'm'
    pre = {3: 'k', 6: 'M', 9: 'G', 12: 'T', 15: 'P', 18: 'E', 21: 'Z', 24: 'Y'}
    for p in list(pre.keys())[::-1]:
        if len(str(x)) > p:
            int_part = str(x)[:-p]
            dec_part = str(x)[-p:]
            dec_part = (dec_part if len(dec_part) <= 3 else dec_part[:3]).rstrip('0') if int(dec_part) > 0 else ''
            return '{}.{}{}m'.format(int_part, dec_part, pre[p]) if dec_part else '{}{}m'.format(int_part, pre[p])
