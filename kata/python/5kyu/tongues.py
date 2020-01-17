def tongues(code):
    v = 'aiyeou'
    c = 'bkxznhdcwgpvjqtsrlmf'
    out = ''
    for i, ch in enumerate(code):
        if ch.isalpha():
            ch = v[(v.index(ch.lower()) + 3) % len(v)] if ch.lower() in v else c[(c.index(ch.lower()) + 10) % len(c)]
            ch = ch.upper() if code[i].isupper() else ch
        out += ch
    return out
