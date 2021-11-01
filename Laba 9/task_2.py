class Node():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def get_value(self):
        return self.value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def __str__(self):
        return str(self.value)

class BinTree:
    def __init__ (self):
        self.start = None
        self.length = 0
        self.last = None

    def add(self, value):
        elem = Node(value)
        if self.start is None:
            self.start = elem
            self.length = 1
        else:
            self.current = self.start
            while True:
                if self.current.value >= value:
                    if self.current.left == None:
                        self.current.left = elem
                        break
                    else:
                        self.current = self.current.left
                else:
                    if self.current.right == None:
                        self.current.right = elem
                        break
                    else:
                        self.current = self.current.right
            self.length += 1

    def __len__(self):
        return self.length

    def __iter__(self):
        res = []
        stack = []
        A = self.start
        while A or stack:
            while A:
                stack.append(A)
                res.append(A)
                A = A.left
            if stack:
                A = stack.pop()
                A = A.right
        return iter(res)


tree = BinTree()
for i in [1,6,4,3,2,8,9]:
    tree.add(i)

for i in tree:
    print(i)
