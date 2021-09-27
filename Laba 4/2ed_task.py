def how_many(func):
    def wrapper(res):
        if func(A) == 0:
            print("Нет:(")
        elif func(A) > 10:
            print("Очень много")
        else:
            print(func(A))
    return wrapper

A = list(map(int, input().split()))

@how_many
def even(A):
    e = 0
    for number in A:
        if number%2 == 0:
            e+=1
    return e

even(A)