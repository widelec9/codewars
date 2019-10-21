import re


def replace(match):
    char = match.group(0)
    if char.islower():
        return str(ord(char) - ord('a') + 1) + ' '
    elif char.isupper():
        return str(ord(char) - ord('A') + 1) + ' '
    else:
        return ''


def alphabet_position(text):
    return re.compile("[a-z\d\s\.\'-]", re.IGNORECASE).sub(replace, text)[:-1]