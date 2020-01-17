def diag_2_sym(s):
    return '\n'.join(map(''.join, list(zip(*[[c for c in ss] for ss in s.split('\n')][::-1]))[::-1]))


def rot_90_counter(s):
    return '\n'.join(map(''.join, list(zip(*[[c for c in ss] for ss in s.split('\n')]))[::-1]))


def selfie_diag2_counterclock(s):
    s1 = [ss for ss in s.split('\n')]
    s2 = diag_2_sym(s).split('\n')
    s3 = rot_90_counter(s).split('\n')
    return '\n'.join(['{}|{}|{}'.format(s1[i], s2[i], s3[i]) for i in range(len(s1))])


def oper(fct, s):
    return fct(s)

