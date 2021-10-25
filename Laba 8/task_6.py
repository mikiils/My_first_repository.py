import itertools
''' Все возможные комбинации из символов в строке s с длинами <= k '''
def get_combinations(s, k):
    l = []
    for n in range(1, k+1):
        c = itertools.combinations(s, n)
        res = []
        d = ''
        for x in c:
            for i in range(n):
                d += x[i]
            res.append(d)
            d = ''
        res.sort()
        print(*res, end = ' ')
    return 0

get_combinations("cat", 2)
#["a", "c", "t", "ac", "at", "ct"]