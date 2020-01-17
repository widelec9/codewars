def tickets(people):
    cash = []
    while people:
        p = people.pop(0)
        if p == 25:
            cash.append(p)
        elif p == 50 and cash.count(25):
            cash.append(p)
            cash.remove(25)
        elif p == 100:
            if cash.count(50) and cash.count(25):
                cash.append(100)
                cash.remove(50)
                cash.remove(25)
            elif cash.count(25) >= 3:
                cash.append(100)
                for _ in range(3):
                    cash.remove(25)
            else:
                return 'NO'
        else:
            return 'NO'
    return 'YES'
