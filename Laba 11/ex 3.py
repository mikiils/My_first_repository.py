import threading
import random
import time
import sys

N = 1
Sum = 0
array = [i for i in range(20,35)]
length = len(array)

def summing (arg):
    global length
    global N
    global array
    global Sum
    st = round(length/N * (arg))
    fin = round(length/N * (arg+1))
    s = 0
    if fin > length:
        fin = length
    for i in range (st, fin):
        s+= array[i]
    Sum += s


start = time.time()

threads = [ threading.Thread(target=summing, args=(i,)) for i in range(N) ]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(time.time() - start)