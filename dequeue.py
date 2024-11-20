'''
@Sidharth Sahoo
Dequeue is a linear data stature which follows last in last out (LILO/FIFO) principle and
it allows insertion and deletion in both side
'''


class DequeueUsingList:
    def __init__(self):
        self.dqqueue = []

    def is_empty(self):
        return not self.dqqueue

    def insert_at_first(self, val):
        self.dqqueue.insert(0, val)

    def insert_at_rear(self, val):
        self.dqqueue.append(val)

    def delete_at_first(self):
        self.dqqueue.pop(0)

    def delete_at_rear(self):
        self.dqqueue.pop()

    def size(self):
        return len(self.dqqueue)


class Node:
    def __init__(self, item=None, next=None, prev=None):
        self.item = item
        self.next = next
        self.prev = prev

class DequeueUsingDLL:
    def __init__(self):
        self.first = None
        self.rear = None
        self.count = 0

    def is_empty(self):
        return not self.first
    def insert_at_first(self, val):
        node = Node(val, self.first)
        if self.is_empty():
            self.first = self.rear = node
        else:
            self.first = node
        self.count += 1
    def insert_at_rear(self, val):
        node = Node(val, prev=self.rear)
        if self.is_empty():
            self.insert_at_first(val)
        else:
            self.rear = node
        self.count += 1
    def delete_at_first(self):
        if self.is_empty():
            raise IndexError('No record found!')
        elif self.first == self.rear:
            self.first = self.rear = None
        else:
            self.first = self.first.next
            self.first.prev = None
        self.count -= 1
    def delete_at_rear(self):
        if self.is_empty() or self.first == self.rear:
            self.delete_at_first()
        else:
            self.rear.prev.next = None
        self.count -= 1

    def size(self):
        return self.count


if __name__ == '__main__':
    dq_using_list = DequeueUsingList()
    dq_using_list.insert_at_first(10)
    dq_using_list.insert_at_first(20)
    dq_using_list.insert_at_rear(30)
    dq_using_list.insert_at_rear(40)
    dq_using_list.insert_at_first(50)
    dq_using_list.insert_at_rear(60)
    dq_using_list.delete_at_first()
    dq_using_list.delete_at_rear()
    print(dq_using_list.size())
    print('------------------------------------------------------')

    dq_using_dll = DequeueUsingDLL()
    dq_using_dll.insert_at_first(10)
    dq_using_dll.insert_at_first(20)
    dq_using_dll.insert_at_rear(30)
    dq_using_dll.insert_at_rear(40)
    dq_using_dll.insert_at_first(50)
    dq_using_dll.insert_at_rear(60)
    dq_using_dll.delete_at_first()
    dq_using_dll.delete_at_rear()
    print(dq_using_dll.size())