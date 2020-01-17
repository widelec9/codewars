def luck_check(n):
    int(n)
    if len(n) % 2:
        return sum(map(int, n[:len(n)//2])) == sum(map(int, n[(len(n)//2)+1:]))
    return sum(map(int, n[:len(n)//2])) == sum(map(int, n[(len(n)//2):]))
