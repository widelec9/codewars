def DNA_strand(dna):
    dic = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([dic[c] for c in dna])