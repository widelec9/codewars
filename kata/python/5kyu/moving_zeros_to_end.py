def move_zeros(array):
    return array + [array.pop(i) for i in range(len(array)-1,-1,-1) if type(array[i]) in [int, float] and array[i] == 0]
