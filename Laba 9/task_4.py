class PrintAverage(Exception):
    pass

class PrintVariance(Exception):
    pass

class PrintQuantity(Exception):
    pass

def sum_coroutine():
    A = []
    s = 0
    n = 0
    try:
        while True:
            try:
                x = yield
                A.append(x)
                s += x
                n += 1
            except PrintAverage:
                yield s/n
            except PrintVariance:
                m = 0
                for el in A:
                    m += (el - s/n)**2
                yield m/n
            except PrintQuantity:
                yield n
    finally:
        print()

coroutine = sum_coroutine()
next(coroutine)
for i in range(12):
    coroutine.send(i)

print("Average is:", coroutine.throw(PrintAverage))
next(coroutine)

print("Variance is:", coroutine.throw(PrintVariance))
next(coroutine)

print("Quantity is:", coroutine.throw(PrintQuantity))
next(coroutine)
coroutine.close()


'''для ввода данных с клавиатуры:
i = int(input())
while i != 0:
    coroutine.send(i)'''