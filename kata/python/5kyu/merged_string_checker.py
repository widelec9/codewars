def is_merge(s, part1, part2):
    back_check = False
    while s:
        if part1 and s[-1] == part1[-1]:
            part1 = part1[:-1]
            s = s[:-1]
            back_check = True
        elif part2 and s[-1] == part2[-1]:
            part2 = part2[:-1]
            s = s[:-1]
            back_check = False
        elif back_check and len(part2) > 1 and s[-1] == part2[-2]:
            part1 += part2[-1]
            part2 = part2[:-2]
            s = s[:-1]
            back_check = False
        else:
            return False
    return False if part1 or part2 else True
