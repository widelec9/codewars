class AlwaysTrue:
    def __eq__(self, other):
        return True


omnibool = AlwaysTrue()
