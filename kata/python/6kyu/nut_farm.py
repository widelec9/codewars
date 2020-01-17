def shake_tree(tree):
    nuts = [1 if c == 'o' else 0 for c in tree.pop(0)]
    while len(tree) > 0:
        for i, c in enumerate(tree[0]):
            if nuts[i] > 0 and c in ['\\', '/', '_']:
                if c == '\\' and i < len(nuts) - 1:
                    nuts[i+1] += nuts[i]
                elif c == '/' and i > 0:
                    nuts[i-1] += nuts[i]
                nuts[i] = 0
        tree.pop(0)
    return nuts