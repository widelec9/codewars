def flap_display(lines, rotors):
    newlines = []
    while len(lines) > 0:
        line = lines.pop(0)
        rot = rotors.pop(0)
        newstr = ''
        for i, r in enumerate(rot):
            line = ''.join([ALPHABET[(ALPHABET.index(c) + r) % len(ALPHABET)] for c in line])
            newstr += line[i]
        newlines.append(newstr)
    return newlines
