def rot_90_clock(s):
    return '\n'.join(map(''.join, zip(*[[c for c in ss] for ss in s.split('\n')][::-1])))


def diag_1_sym(s):
    return '\n'.join(map(''.join, zip(*[[c for c in ss] for ss in s.split('\n')])))


def selfie_and_diag1(s):
    s1 = [ss for ss in s.split('\n')]
    s2 = diag_1_sym(s).split('\n')
    return '\n'.join(['{}|{}'.format(s1[i], s2[i]) for i in range(len(s1))])


def oper(fct, s):
    return fct(s)
