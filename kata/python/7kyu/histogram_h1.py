def histogram(results):
    return ''.join(['{idx}|{h} {cnt}\n'.format(idx=len(results) - i, h='#' * r, cnt=r) if r > 0 else '{idx}|\n'.format(idx=len(results)-i) for i, r in enumerate(reversed(results))])
