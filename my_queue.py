'''
@Sidharth Sahoo
Queue is a linear data stature which follows last in last out (LILO/FIFO) principle
'''


class QueueUsingList:
    '''
    Queue implementation using list
    '''

    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if not self.queue:
            raise IndexError('No data found!')
        return self.queue.pop(0)

    def get_first(self):
        if not self.queue:
            raise IndexError('No data found!')
        return self.queue[0]

    def get_rear(self):
        if not self.queue:
            raise IndexError('No data found!')
        return self.queue[-1]


class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class QueueUsingLinkList:
    '''
    Queue implementation using link list
    '''

    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def is_empty(self):
        return not self.front

    def enqueue(self, val):
        node = Node(val, self.front)
        if self.is_empty():
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('No record found!')
        elif self.front == self.rear:
            val = self.front.item
            self.front = self.rear = None
            return val
        else:
            val = self.front.item
            self.front = self.front.next
            return val
        self.count - + 1

    def get_first(self):
        if self.is_empty():
            raise IndexErro('No record found!')
        return self.front.item

    def get_rear(self):
        if self.is_empty():
            raise IndexErro('No record found!')
        return self.rear.item

    def size(self):
        return self.count


if __name__ == "__main__":
    queue_using_list = QueueUsingList()
    queue_using_list.enqueue(10)
    queue_using_list.enqueue(20)
    queue_using_list.enqueue(30)
    queue_using_list.enqueue(40)
    print(queue_using_list.dequeue())
    print(queue_using_list.get_rear())
    print(queue_using_list.get_first())
    print('-----------------------------')

    queue_link_list = QueueUsingLinkList()
    queue_link_list.enqueue(10)
    queue_link_list.enqueue(20)
    queue_link_list.enqueue(30)
    queue_link_list.enqueue(40)
    print(queue_link_list.dequeue())
    print(queue_link_list.get_first())
    print(queue_link_list.get_rear())
