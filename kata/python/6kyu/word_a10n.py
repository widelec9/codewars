import re


def abbreviate(s):
    for d in re.split(r'[\s;:.\',_\d-]\s*', s):
        if len(d) >= 4:
            s = s.replace(d, d[0] + str(len(d[1:-1])) + d[-1])
    return s