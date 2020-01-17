def zero(*args):
    return 0 if len(args) == 0 else selector(0, args[0][0], args[0][1])
def one(*args):
    return 1 if len(args) == 0 else selector(1, args[0][0], args[0][1])
def two(*args):
    return 2 if len(args) == 0 else selector(2, args[0][0], args[0][1])
def three(*args):
    return 3 if len(args) == 0 else selector(3, args[0][0], args[0][1])
def four(*args):
    return 4 if len(args) == 0 else selector(4, args[0][0], args[0][1])
def five(*args):
    return 5 if len(args) == 0 else selector(5, args[0][0], args[0][1])
def six(*args):
    return 6 if len(args) == 0 else selector(6, args[0][0], args[0][1])
def seven(*args):
    return 7 if len(args) == 0 else selector(7, args[0][0], args[0][1])
def eight(*args):
    return 8 if len(args) == 0 else selector(8, args[0][0], args[0][1])
def nine(*args):
    return 9 if len(args) == 0 else selector(9, args[0][0], args[0][1])

def selector(op1, op2, operation):
    if operation == '+':
        return plus(op1, op2)[1]
    elif operation == '-':
        return minus(op1, op2)[1]
    elif operation == '*':
        return times(op1, op2)[1]
    elif operation == '/':
        return divided_by(op1, op2)[1]

def plus(*args):
    return args[0], '+' if len(args) == 1 else args[0] + args[1]

def minus(*args):
    return args[0], '-' if len(args) == 1 else args[0] - args[1]

def times(*args):
    return args[0], '*' if len(args) == 1 else args[0] * args[1]

def divided_by(*args):
    return args[0], '/' if len(args) == 1 else int(args[0] / args[1])
