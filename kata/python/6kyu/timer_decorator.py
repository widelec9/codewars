from time import sleep


def timer(limit):
    from time import time
    def decorator(f):
        def wrapper(*args, **kwargs):
            tstart = time()
            f(*args, **kwargs)
            return time() - tstart < limit
        return wrapper
    return decorator
