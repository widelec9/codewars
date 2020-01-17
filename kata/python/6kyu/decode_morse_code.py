import re


def decodeMorse(morse_code):
    morse_code = morse_code.lstrip().rstrip()
    for i, word in enumerate(morse_code.split('   ')):
        for j, c in enumerate(word.split(' ')):
            morse_code = morse_code.replace(c, MORSE_CODE[c], 1)
    return re.sub(r'\s{1,2}(\S)', r'\1', morse_code)
