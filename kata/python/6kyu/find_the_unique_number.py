def find_uniq(arr):
    for n in set(arr):
        if arr.count(n) == 1:
            return n