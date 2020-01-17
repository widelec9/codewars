class Robot:
    def __init__(self):
        self.known = list(set('thank you for teaching me'.split() + 'i already know the word'.split() + 'i do not understand the input'.split()))

    def learn_word(self, w):
        if not w:
            return 'I do not understand the input'
        for ch in w:
            if not ch.isalpha():
                return 'I do not understand the input'
        if w.lower() not in self.known:
            self.known += [w.lower()]
            return 'Thank you for teaching me ' + w
        else:
            return 'I already know the word ' + w
