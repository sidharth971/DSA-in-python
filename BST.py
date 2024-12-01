'''
@Sidharth Sahoo
Binary Search Tree is a non linear data structure.
'''

class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self.__insert(val)

    def __insert(self, val):
        if not self.root:
            return Node(val)
        if val < self.root.item:
            self.root.left = self.__insert(val)
        else:
            self.root.right = self.__insert(val)
        return self.root
    def search(self, val):
        return self.__search(val, self.root)

    def __search(self, val, node):
        if not node:
            return False
        if val == node.item:
            return True
        elif val < node.item:
            return self.__search(val, node.left)
        elif val > node.item:
            return self.__search(val, node.right)
    def preorder(self, node):
        if node:
            print(node.item)
            self.preorder(node.left)
            self.preorder(node.right)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.item)
            self.inorder(node.right)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.item)

