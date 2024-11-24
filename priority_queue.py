'''
@Sidharth Sahoo
Priority queue is a linear data structure which stores data based on priority of element
'''


class PriorityQueue:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority


class PriorityQueueUsingList:
    def __init__(self):
        self.queue = []

    def push(self, val):
        index = 0
        while len(self.queue) > index and self.queue[index].priority <= val.priority:
            index += 1

        self.queue.insert(index, val)

    def pop(self):
        return self.queue.pop(0).item

    def size(self):
        return len(self.queue)


class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class PriorityQueueUsingLinkList:
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return not self.head

    def push(self, val):
        node = Node(val)
        if self.is_empty():
            self.head = node
            return

        temp = self.head
        while temp and temp.next:
            temp = temp.next
        temp.next = node
        self.count += 1
        return

    def pop(self):
        if not self.head:
            raise IndexError('No record found!')
        val = self.head.item.item
        self.head = self.head.next
        self.count -= 1
        return val

    def size(self):
        return self.count


if __name__ == '__main__':
    prt_using_list = PriorityQueueUsingList()
    for x in range(1, 7):
        prt = PriorityQueue(x * 10, x)
        prt_using_list.push(prt)

    while prt_using_list.queue:
        print(prt_using_list.pop())

    print('----------------')

    prt_using_link_list = PriorityQueueUsingLinkList()
    for x in range(1, 7):
        prt = PriorityQueue(x * 10, x)
        prt_using_link_list.push(prt)

    while prt_using_link_list.head:
        print(prt_using_link_list.pop())
