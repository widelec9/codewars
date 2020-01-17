def generate_hashtag(s):
    out = '#' + ''.join([w.capitalize() for w in s.split()])
    return out if s != '' and len(out) <= 140 else False
