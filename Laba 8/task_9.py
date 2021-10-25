import itertools
''' Dернуть максимум, который достигает выражение (a_1^2 + a_2^2 + ... + a_n^2) % m . 
Где ai --- максимальный элемент из i-ого списка '''

def maximize(lists, m):
    res = 0
    for i in range(len(lists)):
        res += max(lists[i])**2
    return res % m
lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]

print(maximize(lists, m=1000))
#206