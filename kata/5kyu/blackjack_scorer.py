def score_hand(cards):
    score = sum([int(card) if card.isnumeric() else 10 if card != 'A' else 0 for card in cards])
    aces = cards.count('A')
    while aces:
        diff = 21 - score
        if diff >= 11 and diff-11 >= aces-1:
            score += 11
        else:
            score += 1
        aces -= 1
    return score
