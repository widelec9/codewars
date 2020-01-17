import re


def decodeMorse(morse_code):
    MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                  '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                  '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                  '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
                  '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',',
                  '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
                  '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"',
                  '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}
    morse_code = morse_code.lstrip().rstrip()
    for i, word in enumerate(morse_code.split('  ')):
        for j, c in enumerate(word.split(' ')):
            morse_code = morse_code.replace(c, MORSE_CODE[c], 1)
    return re.sub(r'\s(\S)', r'\1', morse_code)


def decodeBits(bits):
    bit_timing = min(len(seq) for seq in re.findall(r'0+|1+', bits.strip('0')))
    bits = ''.join([bits[i] for i in range(0, len(bits), bit_timing)])
    return bits.replace('111', '-').replace('000', ' ').replace('1', '.').replace('0', '')
