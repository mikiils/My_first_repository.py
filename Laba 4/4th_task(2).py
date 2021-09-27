import time

def decorator(filee):
    def swap(func):
        def wrapped(f_arg1, f_arg2):
            array = []
            array.append(time.perf_counter_ns())
            array.append(f_arg1 + ' ' + f_arg2)
            array.append(func(f_arg1, f_arg2))
            array.append(time.perf_counter_ns())
            array.append(array[3] - array[0])
            file = open(filee, "w")
            array = map(lambda x: str(x) + '\n', array)
            file.writelines(array)
            file.close()
            return array
        return wrapped
    return swap

@decorator("text2.txt")
def function(first, second):
    return int(first) + int(second)

function("10", "15")
