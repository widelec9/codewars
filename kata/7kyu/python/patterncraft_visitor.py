class Marine:
    def __init__(self):
        self.health = 100

    def accept(self, visitor):
        visitor.visit_light(self)


class Marauder:
    def __init__(self):
        self.health = 125

    def accept(self, visitor):
        visitor.visit_armored(self)


class TankBullet:
    def visit_light(self, unit):
        unit.health -= 21

    def visit_armored(self, unit):
        unit.health -= 32
