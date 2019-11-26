import json


def jsonattr(filepath):
    def dec(cls):
        with open(filepath) as file:
            for k, v in json.load(file).items():
                setattr(cls, k, v)
        return cls
    return dec
