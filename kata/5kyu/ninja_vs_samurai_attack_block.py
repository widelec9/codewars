Position = {'high': 'h', 'low': 'l'}  # don't change this!


class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.block = ""
        self.deceased = False
        self.zombie = False

    def attack(self, enemy, position):
        dmg = 0
        if enemy.block != position:
            dmg += 10 if position == Position['high'] else 5
        if not enemy.block:
            dmg += 5
        enemy.set_health(enemy.health - dmg)

    def set_health(self, new_health):
        if not self.health:
            self.zombie = True
        else:
            self.health = new_health if new_health > 0 else 0
            if not self.health:
                self.deceased = True
