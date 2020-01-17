def data_reverse(data):
    bytes = []
    while len(data) > 0:
        bytes.append(''.join([str(data[i]) for i in range(0, 8)]))
        data = data[8:]
    bytes.reverse()
    return [int(b[i]) for b in bytes for i in range(0, 8)]