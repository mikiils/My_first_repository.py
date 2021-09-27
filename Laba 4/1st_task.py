import sys
import argparse

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-n')
    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    n = int(namespace.n)
    f1 = f2 = 1
    for i in range(2, n):
        f1, f2 = f2, f1 + f2
    print(f2)

# python 1st_task.py -n 9