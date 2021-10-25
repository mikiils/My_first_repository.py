import itertools
''' Все возможные комбинации из символов в строке s с длинами = k с повторениями '''

def get_combinations_with_r(s, n):
    c = itertools.combinations_with_replacement(s,n)
    res = []
    d = ''
    for x in c:
        for i in range(n):
            d += x[i]
        res.append(d)
        d = ''
    res.sort()
    return res

print(get_combinations_with_r("cat", 2))
#["aa", "at", "ca", "cc", "ct", "tt"]