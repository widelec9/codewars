def rot_90(s, d=1):
    if d:
        return '\n'.join(map(''.join, zip(*[[c for c in ss] for ss in s.split('\n')][::-1])))
    return '\n'.join(map(''.join, list(zip(*[[c for c in ss] for ss in s.split('\n')]))[::-1]))


def code(s):
    if not s:
        return ''
    l = len(s)**0.5
    n = int(l) if l.is_integer() else int(l) + 1
    if n > l:
        s += '\x0b' * (n**2 - len(s))
    return rot_90('\n'.join([s[i:i+n] for i in range(0, len(s), n)]))


def decode(s):
    if not s:
        return ''
    return rot_90(s, 0).replace('\n', '').rstrip('\x0b')
