class CaesarCipher(object):
    def __init__(self, shift):
        self.sh = shift

    def encode(self, s):
        return ''.join([chr((((ord(ch.upper()) + self.sh) - ord('A')) % 26) + ord('A')) if ch.isalpha() else ch for i, ch in enumerate(s)])

    def decode(self, s):
        return ''.join([chr((((ord(ch.upper()) - self.sh) + ord('A')) % 26) + ord('A')) if ch.isalpha() else ch for i, ch in enumerate(s)])
