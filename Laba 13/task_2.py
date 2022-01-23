'''
Программа принимает от пользователя команды:
add X - добавить элемент в дерево;
find X - найти элемент в дереве;
delete X - удалить элемент из дерева;
print - распечатать все элементы дерева в отсортированном порядке;
clear - очистить дерево;
dump - создать резервную копию дерева;
exit - завершить работу.
'''
import pickle

class Node:
    def __init__(self, cur):
        self.cur = cur
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.cur):
            if(node.left != None):
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if(node.right != None):
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.cur):
            return node
        elif (val < node.cur and node.left != None):
            self._find(val, node.left)
        elif (val > node.cur and node.right != None):
            self._find(val, node.right)

    def delete(self, val):


    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)
        

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print (str(node.v) + ' ')
            self._printTree(node.r)


if __name__ == "__main__":

    try:
        with open('data.pickle', "rb") as f:
            tree = pickle.load(f)
    except Exception:
        f = open("data.pickle", "wb")
        tree =
    cc = input()
    while cc != 'exit':

    close()
