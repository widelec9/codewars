class SiegeState:
    def __init__(self):
        self.move = False
        self.dmg = 20


class TankState:
    def __init__(self):
        self.move = True
        self.dmg = 5


class Tank:
    def __init__(self):
        self.state = TankState()

    def can_move(self):
        return self.state.move

    def damage(self):
        return self.state.dmg
