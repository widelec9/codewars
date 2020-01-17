def to_underscore(string):
    if type(string) == int:
        return str(string)
    out = []
    i = 0
    while i < len(string)-1:
        i += 1
        if string[i].isupper():
            out += [string[:i].lower()]
            string = string[i:]
            i = 0
    out += [string.lower()]
    return '_'.join(out)
