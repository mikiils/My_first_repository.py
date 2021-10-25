def fib(N):
    a = 0
    b = 1
    yield b
    t = 2
    while t <= N:
        c = b+a
        yield c
        a, b = b, c
        t += 1

N = int(input())
for i in fib(N):
    print(i, end = " ")