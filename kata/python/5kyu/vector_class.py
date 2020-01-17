class Vector:
    def __init__(self, v):
        self.v1 = v

    def __len__(self):
        return len(self.v1)

    def __getitem__(self, item):
        return self.v1[item]

    def __str__(self):
        return '({})'.format(','.join([str(x) for x in self.v1]))

    def equals(self, v2):
        if len(self.v1) != len(v2):
            return False
        return all([self.v1[i] == v2[i] for i in range(len(self.v1))])

    def add(self, v2):
        if len(self.v1) != len(v2):
            return False
        return Vector([self.v1[i] + v2[i] for i in range(len(self.v1))])

    def subtract(self, v2):
        if len(self.v1) != len(v2):
            return False
        return Vector([self.v1[i] - v2[i] for i in range(len(self.v1))])

    def dot(self, v2):
        if len(self.v1) != len(v2):
            return False
        return sum([self.v1[i] * v2[i] for i in range(len(self.v1))])

    def norm(self):
        return sum([self.v1[i] ** 2 for i in range(len(self.v1))]) ** 0.5
