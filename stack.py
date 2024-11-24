'''
@Sidharth Sahoo
Stack is a linear data stature which follows last in and fast out principle.
'''
from DSA.DSA_in_python.sll import SLL


class StackUsingList(list):
    '''
    Stack extending buit-in list class
    '''

    def is_empty(self):
        return not self

    def push(self, val):
        self.append(val)

    def pop(self):
        if self.is_empty():
            raise IndexError('No record found!')
        return super(StackUsingList, self).pop()

    def peak(self):
        if self.is_empty():
            raise IndexError('No record found!')
        return self[-1]

    def size(self):
        return len(self)

    def insert(self, val, index):
        raise AttributeError('No attribute "insert" found!')


class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class StackUsingLinkList:
    '''
    Stack using link list
    '''

    def __init__(self):
        self.start = None
        self.count = 0

    def is_empty(self):
        return not self.start

    def push(self, val):
        node = Node(val, self.start)
        self.start = node
        self.count += 1

    def peak(self):
        if self.is_empty():
            raise IndexError('No Record found!')
        return self.start.item

    def pop(self):
        if self.is_empty():
            raise IndexError('No Record found!')
        value = self.start.item
        self.start = self.start.next
        self.count -= 1
        return value

    def size(self):
        return self.count


class StackUsingSLL(SLL):
    def __init__(self):
        super(StackUsingSLL, self).__init__()
        self.count = 0

    def push(self, val):
        self.insert_at_first(val)
        self.count += 1

    def pop(self):
        if not self.head:
            raise IndexError('No record found')
        val = self.head.item
        self.head = self.head.next
        return val

    def peak(self):
        if not self.head:
            raise IndexError('No record found')
        return self.head.item

    def size(self):
        return self.count


if __name__ == "__main__":
    stack_list = StackUsingList()
    stack_list.push(10)
    stack_list.push(20)
    stack_list.push(30)
    print(stack_list.peak())
    print(stack_list.pop())
    print(stack_list.size())
    print('------------------------------------------')

    stck_link_list = StackUsingLinkList()
    stck_link_list.push(10)
    stck_link_list.push(20)
    stck_link_list.push(30)
    print(stck_link_list.peak())
    print(stck_link_list.pop())
    print(stck_link_list.size())
    print('------------------------------------------------')

    stck_sll = StackUsingSLL()
    stck_sll.push(10)
    stck_sll.push(20)
    stck_sll.push(30)
    print(stck_sll.pop())
    print(stck_sll.peak())
    print(stck_sll.size())
