import re


def increment_string(string):
    a = re.search('\D*(\d*$)', string)
    return string + '1' if a.group(1) == '' else string[:-len(a.group(1))] + str(int(a.group(1)) + 1).zfill(len(a.group(1)))