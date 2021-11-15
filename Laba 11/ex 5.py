import multiprocessing

def worker():
    LIST.append('item')
    print(LIST)

LIST = []

if __name__ == "__main__":
    processes = [ multiprocessing.Process(target=worker) for _ in range(5) ]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(LIST)

''' Потому что выводится глобальная переменная LIST. А в каждом потоке изменяется локальная'''