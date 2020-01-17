from re import split


def shake_tree(tree):
    nuts = [1 if c == 'o' else 0 for c in tree.pop(0)]
    regex = r'[o.\s]\s*'
    while len(tree) > 0:
        row = tree.pop(0)
        for i, c in enumerate(row):
            if c == 'o':
                nuts[i] += 1
            if nuts[i] > 0 and c in ['\\', '/', '_']:
                if c == 'o':
                    nuts[i] += 1
                elif c == '\\' and i < len(row) - 1:
                    if split(regex, row[i:])[0].count('/') > 0:
                        nuts[i] = 0
                    else:
                        rep_count = split(regex, row[i:])[0].count('\\')
                        nuts[i+rep_count] += nuts[i]
                elif c == '/' and i > 0:
                    if split(regex, row[:i+1])[-1].count('\\') > 0:
                        nuts[i] = 0
                    else:
                        rep_count = split(regex, row[:i+1])[-1].count('/')
                        nuts[i-rep_count] += nuts[i]
                nuts[i] = 0
    return nuts