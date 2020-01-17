def naughty_or_nice(data):
    behavior = sum([list(data[month].values()) for month in data], [])
    if behavior.count('Naughty') > behavior.count('Nice'):
        return 'Naughty!'
    return 'Nice!'
