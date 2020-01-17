def histogram(rolls):
    if rolls != [0, 0, 0, 0, 0, 0]:
        s = ''
        for i in range(max(rolls)+1, 0, -1):
            for r in rolls:
                if i == r + 1 and r != 0:
                    s += str(r)
                    if r < 10:
                        s += ' '
                elif i <= r:
                    s += '# '
                else:
                    s += '  '
            s = s.rstrip() + '\n'
        return s + '-----------\n1 2 3 4 5 6\n'
    else:
        return '\n-----------\n1 2 3 4 5 6\n'