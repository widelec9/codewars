def flatten(*args):
    def extract_gen(lst):
        for item in lst:
            if isinstance(item, (list, tuple)):
                for subitem in extract_gen(item):
                    yield subitem
            else:
                yield item
    return list(extract_gen(list(args)))
