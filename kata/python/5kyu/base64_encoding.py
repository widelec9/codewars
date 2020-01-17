base64 = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')


def to_base_64(string):
    b64out = ''
    padding = (3 - (len(string) % 3)) % 3
    for i in range(0, len(string), 3):
        s = string[i:i + 3].ljust(3, '\0')
        octets_num = ord(s[0]) << 16 | ord(s[1]) << 8 | ord(s[2])
        sextets = [(octets_num >> 18) & 63, (octets_num >> 12) & 63, (octets_num >> 6) & 63, octets_num & 63]
        for sex in sextets:
            b64out += base64[sex]
    return b64out[:len(b64out)-padding]


def from_base_64(string):
    out = ''
    for i in range(0, len(string), 4):
        s = string[i:i+4]
        sextets_num = int()
        for j in range(0, 4):
            try:
                sextets_num |= base64.index(s[j]) << (18 - j*6)
            except IndexError:
                continue
        octets = [(sextets_num >> 16) & 255, (sextets_num >> 8) & 255, sextets_num & 255]
        for oct in octets:
            out += chr(oct)
    return out.rstrip('\x00')