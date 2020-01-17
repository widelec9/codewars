from math import ceil


def encode(s):
    dim = ceil(len(s) ** 0.5)
    sq = [[''] * dim for _ in range(dim)]
    sq_lst = []
    rot = 0
    for i, ch in enumerate(s):
        sq[0][sq[0].index('')] = ch
        sq = list(map(list, zip(*sq)))[::-1]
        rot = (rot + 1) % 4
        if '' not in sq[0] or i == len(s) - 1:
            if rot:
                for j in range(4 - rot):
                    sq = list(map(list, zip(*sq)))[::-1]
            sq_lst += [sq]
            sq = [row[1:-1] for row in sq[1:-1]]
    sh = 1
    while len(sq_lst) > 1:
        sq_lst[0] = sq_lst[0][:sh] + [sq_lst[0][i+sh][:sh] + sq_lst[1][i] + sq_lst[0][i+sh][-sh:] for i, _ in enumerate(sq_lst[1])] + sq_lst[0][-sh:]
        sq_lst.pop(1)
        sh += 1
    return ''.join([c if c != '' else ' ' for c in sum(sq_lst[0], [])])


def decode(s):
    dim = int(len(s) ** 0.5)
    sq = list(map(list, zip(*[iter(s)] * dim)))
    out = ''
    sh = 0
    while len(out) < len(s):
        if sq[0][sh] == '':
            sh += 1
        out += sq[0][sh]
        sq[0][sh] = ''
        if sh == dim - 1:
            sq = [row[1:-1] for row in sq[1:-1]]
            dim = len(sq)
            sh = 0
        else:
            sq = list(map(list, zip(*sq)))[::-1]
    return out.rstrip(' ')
