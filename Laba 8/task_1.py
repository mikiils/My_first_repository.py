def print_map(function, iterable):
    print(*map(function, iterable), sep = ' ')

def print_map_2(function, iterable):
    iterator = iter(iterable)
    k = True
    while k:
        try:
            print(function(next(iterator)), end = ' ')
        except StopIteration:
            k = False

print_map(abs, [1, -1, 5, -6])
print('------------------')
print_map_2(abs, [1, -1, 5, -6])