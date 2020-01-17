def Xbonacci(signature, n):
    b = len(signature)
    while len(signature) < n:
        signature.append(sum(signature[-b:]))
    return signature[:n]