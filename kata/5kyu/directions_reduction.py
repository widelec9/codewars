def dirReduc(arr):
    i = len(arr)
    while i > 0:
        i -= 1
        if i > 0 and ((arr[i-1], arr[i]) == ('NORTH', 'SOUTH') or (arr[i], arr[i-1]) == ('NORTH', 'SOUTH') or (arr[i-1], arr[i]) == ('WEST', 'EAST') or (arr[i], arr[i-1]) == ('WEST', 'EAST')):
            arr.pop(i-1)
            arr.pop(i-1)
            i = len(arr)
    return arr
