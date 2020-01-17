def tour(friends, towns, dists):
    friends_given = [t[0] for t in towns]
    d = dists[towns[friends_given.index(friends[0])][1]]
    last_friend = friends[0]
    for i, f in enumerate(friends[1:]):
        if friends[i+1] in friends_given:
            d += ((dists[towns[[t[0] for t in towns].index(friends[i+1])][1]])**2 - dists[towns[[t[0] for t in towns].index(friends[i])][1]]**2) ** 0.5
            last_friend = friends[i+1]
    return int(d + dists[towns[[t[0] for t in towns].index(last_friend)][1]])
