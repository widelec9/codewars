from itertools import combinations_with_replacement

def find_all(sum_dig, digs):
    range_start = pow(10, digs - 1)
    range_end = pow(10, digs)
    combs = [''.join(i) for i in combinations_with_replacement('0123456789', digs) if range_start < int(''.join(i)) < range_end]
    data = [int(i) for i in combs if sum(map(int, i)) == sum_dig and i == ''.join(sorted(i))]
    return [len(data), min(data), max(data)] if len(data) > 0 else []