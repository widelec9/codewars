class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, activity):
        if activity < -8 or activity > 8 or activity == 0:
            raise Exception
        elif self.rank < 8:
            diff = abs(activity - self.rank) if not (self.rank < 0 < activity) else abs(activity - self.rank) - 1
            if diff == 0:
                self.progress += 3
            elif (diff == 1 and activity < self.rank) or (diff == 2 and activity < 0 < self.rank):
                self.progress += 1
            elif diff > 0 and activity > self.rank:
                self.progress += 10 * (diff ** 2)

            while self.progress >= 100:
                self.rank += 1
                self.progress -= 100
                if self.rank == 0:
                    self.rank += 1
                elif self.rank == 8:
                    self.progress = 0
