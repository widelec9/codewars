def ips_between(start, end):
    start, end = list(map(int, start.split('.'))), list(map(int, end.split('.')))
    diff = [end[i] - start[i] for i in range(len(end))]
    return diff[0]*16777216 + diff[1]*65536 + diff[2]*256 + diff[3]
