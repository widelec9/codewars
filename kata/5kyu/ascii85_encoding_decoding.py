def toAscii85(data):
    data = list(data)
    enc = []
    pad = 0
    while data:
        if len(data) >= 4 and data[:4] == ['\0'] * 4:
            enc += ['z']
            data = data[4:]
            continue
        if len(data) < 4:
            pad = 4 - len(data)
            data += [chr(0)] * pad
        num = ord(data.pop(0)) << 24 | ord(data.pop(0)) << 16 | ord(data.pop(0)) << 8 | ord(data.pop(0))
        a85 = []
        for i in range(5):
            num, m = divmod(num, 85)
            a85 += [chr(m+33)]
        enc += a85[::-1]
    return '<~' + ''.join(enc[:-pad]) + '~>' if pad else '<~' + ''.join(enc) + '~>'


def fromAscii85(data):
    data = [c for c in data if c not in [' ', '\t', '\n']][2:-2]
    dec = []
    pad = 0
    while data:
        if data[0] == 'z':
            dec += ['\0'] * 4
            data.pop(0)
            continue
        if len(data) < 5:
            pad = 5 - len(data)
            data += ['u'] * pad
        num = 0
        for i in range(4, -1, -1):
            num += (ord(data.pop(0)) - 33) * (85**i)
        for i in range(4):
            dec += [chr((num >> (24 - i*8)) & 0xFF)]
    return ''.join(dec[:-pad]) if pad else ''.join(dec)
