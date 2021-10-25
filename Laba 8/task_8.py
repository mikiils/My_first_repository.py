import itertools
''' Количество подряд идующих символов в строке '''

def compress_string(s):
    x = list(s)
    for i, j in itertools.groupby(x):
        print ((len(list (j)), i), end = ' ')
    return 0

compress_string('1222311')
#[(1, 1), (3, 2), (1, 3), (2, 1)]