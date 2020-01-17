def format_duration(seconds):
    if seconds != 0:
        mods = [31536000, 86400, 3600, 60, 1]
        labels = ['year', 'day', 'hour', 'minute', 'second']
        out = []
        for i, m in enumerate(mods):
            out.append(seconds // mods[i])
            seconds -= (out[i] * mods[i])
        outstrings = list()
        for i, o in enumerate(out):
            if o != 0:
                s = '{} {}'.format(o, labels[i])
                if o > 1:
                    s += 's'
                outstrings.append(s)
        return ' and '.join([', '.join(outstrings[:-1])] + [outstrings[-1]]) if len(outstrings) > 1 else outstrings[0]
    else:
        return 'now'