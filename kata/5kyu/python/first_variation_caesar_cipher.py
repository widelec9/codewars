from __future__ import division
from math import ceil


def moving_shift(s, shift):
    mystr = ''
    for c in s:
        shift %= 26
        if c.isalpha():
            if c.isupper() and ord(c) + shift > ord('Z'):
                mystr += chr(ord('A') + shift - (ord('Z') - ord(c)) - 1)
            elif c.islower() and ord(c) + shift > ord('z'):
                mystr += chr(ord('a') + shift - (ord('z') - ord(c)) - 1)
            else:
                mystr += chr(ord(c) + shift)
        else:
            mystr += c
        shift += 1

    str_ret_list = []
    for l in get_len_list(mystr):
        str_ret_list += [mystr[0:int(l)]]
        mystr = mystr[int(l):]
    return str_ret_list


def get_len_list(str):
    l = len(str)
    main = int(ceil(l/5))
    ret_list = list()
    i = 0
    while l >= main:
        ret_list += [main]
        l -= main
        i += 1
    if i < 5:
        ret_list += [l]
        i += 1
        for j in range(i+1, 5):
            ret_list += [0]
    return ret_list


def demoving_shift(s, shift):
    s = ''.join(s)
    mystr = ''
    for c in s:
        shift %= 26
        if c.isalpha():
            if c.isupper() and ord(c) - shift < ord('A'):
                mystr += chr(ord('Z') - (shift + (ord('A') - ord(c)) - 1))
            elif c.islower() and ord(c) - shift < ord('a'):
                mystr += chr(ord('z') - (shift + (ord('a') - ord(c)) - 1))
            else:
                mystr += chr(ord(c) - shift)
        else:
            mystr += c
        shift += 1
    return mystr