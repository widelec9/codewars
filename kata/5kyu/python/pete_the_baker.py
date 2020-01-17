def cakes(recipe, available):
    a = []
    for ing in recipe:
        if ing not in available.keys():
            return 0
        a += [available[ing] // recipe[ing]]
    return min(a)
