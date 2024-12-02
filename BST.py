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
        self.root = self.__insert(self.root, val)

    def __insert(self, node, val):
        if not node:
            return Node(val)
        if val < node.item:
            node.left = self.__insert(node.left, val)
        else:
            node.right = self.__insert(node.right, val)
        return node

    def search(self, val):
        return self.__search(val, self.root)

    def __search(self, val, node):
        if not node:
            return False
        if val == node.item:
            return node.item
        elif val < node.item:
            return self.__search(val, node.left)
        elif val > node.item:
            return self.__search(val, node.right)

    def preorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            result.append(node.item)
            self.preorder(node.left, result)
            self.preorder(node.right, result)
        return result

    def inorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.inorder(node.left, result)
            result.append(node.item)
            self.inorder(node.right, result)
        return result

    def postorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.item)
        return result

    def min_element(self):
        if not self.root:
            return None
        temp = self.root.left
        while temp.left:
            temp = temp.left
        return temp.item

    def max_element(self):
        if not self.root:
            return None
        temp = self.root.right
        while temp.right:
            temp = temp.right
        return temp.item

    def __min_Value(self, node):
        if not node:
            return node
        temp = node
        while temp:
            temp = temp.left
        return temp.item

    def delete(self, val):
        self.root = self.__delete(self.root, val)

    def __delete(self, node, val):
        if not node:
            return Node
        if val > node.item:
            node.right = self.__delete(node.right, val)
        elif val < node.item:
            node.left = self.__delete(node.left, val)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            node.item = self.__min_Value(node.right)
            node.right = self.__delete(node.right, node.item)
        return node

    def size(self):
        return len(self.inorder(self.root))


if __name__ == '__main__':
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(60)
    bst.insert(20)
    bst.insert(70)
    bst.insert(10)
    bst.insert(80)
    bst.insert(95)
    print(bst.search(10))
    print(bst.min_element())
    print(bst.max_element())
    print(bst.size())
    bst.delete(10)
    print(bst.search(10))
    print(bst.preorder(bst.root))
    print(bst.inorder(bst.root))
    print(bst.postorder(bst.root))
