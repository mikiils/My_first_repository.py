def my_zip(*values):
    l = len(values)
    t = 0
    c = []
    while t < len(values[0]):
        for i in range(l):
            c.append(values[i][t])
        yield c
        t+=1
        c = []

def my_map(func, iterible):
    for i in iterible:
        yield func(i)

def my_enumerate(iterible, start = 0):
    i = start
    for x in iterible:
        yield (i, x)
        i+=1




# --------- p r o g r a m -----------

names = ["Alex", "Bob", "Alice", "John", "Ann"]
age = [25, 17, 34, 24, 42]
sex = ["M", "M", "F", "M", "F"]

for values in my_zip(names, age, sex):
    print("name: {:>10} age: {:3} sex: {:2}".format(*values))

# ------------------
print()
# ------------------

def baz(value):
    return value * value

lst = [1, 2, 3, 4, 5]

for i in map(baz, lst):
    print(i)

# ------------------
print()
# ------------------

names = ["Alex", "Bob", "Alice", "John", "Ann"]

for idx, elem in my_enumerate(names, 1):
    print("{:02}: {:>7}".format(idx, elem))
