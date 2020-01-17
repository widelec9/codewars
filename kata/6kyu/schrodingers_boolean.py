class AlwaysTrue:
    def __eq__(self, other):
        return True


omnibool = AlwaysTrue()


print(omnibool == True)
print(omnibool == False)
