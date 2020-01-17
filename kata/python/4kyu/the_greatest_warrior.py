class Warrior:
    def __init__(self):
        self._experience = 100
        self.rank_table = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
        self.achievements = []

    @property
    def experience(self):
        return min(self._experience, 10000)

    @property
    def level(self):
        return self.experience // 100

    @property
    def rank(self):
        return self.rank_table[self.experience // 1000]

    def training(self, train):
        if self.level >= train[2]:
            self.achievements += [train[0]]
            self._experience += train[1]
            return train[0]
        return 'Not strong enough'

    def battle(self, opp_lvl):
        if not 1 <= opp_lvl <= 100:
            return 'Invalid level'
        diff = opp_lvl - self.level
        if diff in [-1, 0]:
            self._experience += 5 if diff == -1 else 10
            return 'A good fight'
        elif diff > 0:
            if diff >= 5 and opp_lvl // 10 > self.level // 10:
                return "You've been defeated"
            self._experience += 20 * diff**2
            return 'An intense fight'
        return 'Easy fight'


# d = Warrior()
# d.experience = 1586
# d.level = 15
# d.rank = d.rank_table[1]
# d.battle(20)

tom = Warrior()
print(tom.level, 1)
print(tom.experience, 100)
print(tom.rank, "Pushover")


bruce_lee = Warrior()
print(bruce_lee.level, 1)
print(bruce_lee.experience, 100)
print(bruce_lee.rank, "Pushover")
print(bruce_lee.achievements, [])
print(bruce_lee.training(["Defeated Chuck Norris", 9000, 1]), "Defeated Chuck Norris")
print(bruce_lee.experience, 9100)
print(bruce_lee.level, 91)
print(bruce_lee.rank, "Master")
print(bruce_lee.battle(90), "A good fight")
print(bruce_lee.experience, 9105)
print(bruce_lee.achievements, ["Defeated Chuck Norris"])
