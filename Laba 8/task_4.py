import itertools

def get_cartesian_product(a, b):
    return itertools.product([1, 2], [3, 4])


print(* get_cartesian_product([1, 2], [3, 4]))
#[(1, 3), (1, 4), (2, 3), (2, 4)]
