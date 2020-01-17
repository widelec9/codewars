def longest_slide_down(pyramid):
    pyramid = [row + [0] * (len(pyramid[-1])-i) for i, row in enumerate(pyramid)]
    for row in range(len(pyramid)-1, 0, -1):
        for i, dig in enumerate(pyramid[row-1][:-1]):
            pyramid[row-1][i] += max(pyramid[row][i], pyramid[row][i+1])
        pyramid = pyramid[:-1]
    return pyramid[0][0]
