def love_language(partner, weeks):
    langs = [['words', 0], ['acts', 0], ['gifts', 0], ['time', 0], ['touch', 0]]
    sh = 0
    for w in range(weeks):
        for d in range(7):
            l = (d + sh) % len(langs)
            langs[l][1] += 1 if partner.response(langs[l][0]) == 'positive' else 0
        sh += 2
    scores = list(zip(*langs))[1]
    return langs[scores.index(max(scores))][0]
