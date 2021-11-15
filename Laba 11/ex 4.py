import urllib.request
import threading
import sys
import time

'''
в среднем 2,3 сек исполнялся код без потоков
1 сек с потоками :)
'''

urls = [ 'https://www.yandex.ru', 'https://www.google.com', 'https://habrahabr.ru', 'https://www.python.org', 'https://isocpp.org' ]

def read_url(url):
    with urllib.request.urlopen(url) as u:
        return u.read()

start = time.time()

threads = [ threading.Thread(target=read_url, args=(url,)) for url in urls ]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(time.time() - start)