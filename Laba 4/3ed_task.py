def swap(func):
    def ww(x, y, show=False):
        print(func(y, x, show=False))
    return ww


@swap
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res

div(2, 4, show=True)