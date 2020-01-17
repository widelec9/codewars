class Fly:
    def move(self, unit):
        unit.position += 10


class Walk:
    def move(self, unit):
        unit.position += 1


class Viking:
    def __init__(self):
        self.move_behavior = Walk()
        self.position = 0

    def move(self):
        self.move_behavior.move(self)
