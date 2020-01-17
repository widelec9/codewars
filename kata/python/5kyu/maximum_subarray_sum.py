def maxSequence(arr):
    if not arr or all([x < 0 for x in arr]):
        return 0
    local_max = [arr[0]]
    for i in range(1, len(arr)):
        local_max += [max(arr[i], arr[i]+local_max[i-1])]
    return max(local_max)
