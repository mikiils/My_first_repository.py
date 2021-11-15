import threading
import random
import time
import sys


def thread_job():
    global counter
    old_counter = counter
    w = random.randint(0, 2)
    #print('сплю', format(w), 'секунд')
    time.sleep(w)
    counter = old_counter + 1
    print('{} '.format(counter), end='')
    sys.stdout.flush()


counter = 0
threads = [threading.Thread(target=thread_job) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print()
print(counter)

'''Это происходит потому что некоторые запущенные при помощи .start() потоки выполныются быстрее
и join-у не приходится их ждать
в первой версии программы counter при вызове start мгновенно изменялся и успевал до запуска след. потока
поэтому пробегались все значения от 1 до 10. Здесь же из-за задержки counter не успевает измениться

Решение:
import threading
import random
import time
import sys

def thread_job():
    lock.acquire()  # mutex
    global counter
    old_counter = counter
    time.sleep(random.randint(0, 1))
    counter = old_counter + 1
    print('{} '.format(counter), end='')
    sys.stdout.flush()
    lock.release()

lock = threading.Lock()
counter = 0
threads = [threading.Thread(target=thread_job) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(counter)

(((  или просто with lock: в начале ф-ции thread_job  - "контекстный менеджер")))'''
