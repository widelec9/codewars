from itertools import product


def rolldice_sum_prob(sum_, dice_amount):
    all_prods = [i for i in product(list(range(1, 7)), repeat=dice_amount)]
    return len([i for i in all_prods if sum(i) == sum_]) / len(all_prods)