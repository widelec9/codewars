def make_readable(seconds):
    return '{h:02d}:{m:02d}:{s:02d}'.format(h=seconds//3600, m=(seconds%3600)//60, s=seconds%60)
