def first_non_repeating_letter(string):
    for i, c in enumerate(string.lower()):
        if string.lower().count(c) == 1:
            return string[i]
    return ''
