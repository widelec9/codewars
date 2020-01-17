def rgb(r, g, b):
    ret = str()
    for i in [r, g, b]:
        i = 0x00 if i < 0x00 else 0xFF if i > 0xFF else i
        ret += format(i, '02x').upper()
    return ret