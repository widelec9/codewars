class Automaton(object):
    def __init__(self):
        self.trans = {1: {0: 1, 1: 2},
                      2: {0: 3, 1: 2},
                      3: {0: 2, 1: 2}}
        self.state = 1

    def read_commands(self, commands):
        for cmd in commands:
            self.state = self.trans[self.state][int(cmd)]
        return self.state == 2


my_automaton = Automaton()