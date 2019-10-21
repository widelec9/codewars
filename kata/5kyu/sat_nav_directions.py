from operator import add
from collections import OrderedDict


def sat_nav(directions):
    pos = [0, 0]
    heading = str()
    mov_dict = OrderedDict({'NORTH': [0, 1], 'EAST': [1, 0], 'SOUTH': [0, -1], 'WEST': [-1, 0]})
    while len(directions) > 0:
        msg = directions.pop(0)
        if 'Head' in msg:
            heading = msg.split(' ')[1]
        elif 'Take the' in msg:
            when = 1 if msg.split(' ')[2] == 'NEXT' else int(msg.split(' ')[2][0])
            while when > 0:
                if pos[0] % 10 != 0:
                    dist = pos[0] % 10
                    if heading == 'EAST': dist = 10 - dist
                elif pos[1] % 10 != 0:
                    dist = pos[1] % 10
                    if heading == 'NORTH': dist = 10 - dist
                else:
                    dist = 10
                pos = list(map(add, pos, [i * dist for i in mov_dict[heading]]))
                when -= 1
            turn = -1 if msg.split(' ')[3] == 'LEFT' else 1
            heading = list(mov_dict.keys())[(list(mov_dict.keys()).index(heading) + turn) % len(mov_dict)]
        elif 'Go straight on for' in msg:
            dist = int(float(msg.split(' ')[4][:-2]) * 10) if 'km' in msg else int(int(msg.split(' ')[4][:-1]) / 100)
            pos = list(map(add, pos, [i * dist for i in mov_dict[heading]]))
        elif 'Turn around' in msg:
            heading = list(mov_dict.keys())[(list(mov_dict.keys()).index(heading) + 2) % len(mov_dict)]
    return pos
