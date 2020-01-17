import itertools


def permutations(string):
	return [''.join(c) for c in set(itertools.permutations(string))]