import pickle
from collections import deque

'''
I/O объекты (результат open()) - НЕЛЬЗЯ: cannot pickle '_io.TextIOWrapper' object
итераторы - МОЖНО
встроенные функции (например, print или abs) - МОЖНО
функции и классы из подключенных библиотек - МОЖНО
самописные функции и классы - МОЖНО
'''

def t(a):
    return a*a

data = {
    'a': [i for i in range(10)],
    #'b': open('data.pickle', 'r'),
    'c': print(),
    'd': deque,
    'e': t(25)
}
print (data)
with open('what,s_name', 'wb') as f:
    pickle.dump (data, f, pickle.HIGHEST_PROTOCOL)
with open('what,s_name', 'rb') as f:
    first = pickle.load(f)
print(first)
