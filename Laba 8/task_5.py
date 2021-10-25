import itertools
''' Перестановки из n символов в строке s в лексикографическом(!) порядке'''
def get_permutations(s, n):
    c = itertools.permutations(s, n)
    res = []
    d = ''
    for x in c:
        for i in range(n):
            d += x[i]
        res.append(d)
        d = ''
    res.sort()
    return res

print(get_permutations("cat", 2))
#["ac", "at", "ca", "ct", "ta", "tc"]