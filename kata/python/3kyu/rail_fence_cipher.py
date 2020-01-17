def encode_rail_fence_cipher(string, n):
    out = [[] for x in range(n)]
    delta = 1
    rail = 0
    for c in string:
        out[rail] += c
        rail += delta
        delta = -1 if rail == n - 1 else 1 if rail == 0 else delta
    return ''.join(sum(out, []))


def decode_rail_fence_cipher(string, n):
    if string == '':
        return ''
    else:
        out = ['' for x in range(len(string))]
        indices = [[] for x in range(n)]
        shift = (2*n)-2
        for rail in range(n):
            i = 0
            while rail + i*shift < len(string):
                indices[rail] += [rail + i*shift]
                i += 1
        for rail in range(n):
            for i in range(len(indices[rail])):
                new_idx = indices[rail][i] + shift - rail*2
                if 0 < new_idx < len(string) and new_idx not in indices[rail]:
                    indices[rail] += [new_idx]
            indices[rail] = sorted(indices[rail])
        for i, pos in enumerate(sum(indices, [])):
            out[pos] = string[i]
        return ''.join(out)