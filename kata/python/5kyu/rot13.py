def rot13(message):
    msg = str()
    for c in message:
        if c.islower():
            bound = ['a', 'z']
        elif c.isupper():
            bound = ['A', 'Z']
        else:
            msg += c
            continue
        if ord(c) + 13 <= ord(bound[1]):
            msg += chr(ord(c) + 13)
        else:
            msg += chr(ord(bound[0]) + (13 - (ord(bound[1]) - ord(c)) - 1))
    return msg