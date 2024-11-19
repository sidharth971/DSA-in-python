'''
@Sidharth Sahoo
Queue is alinear data strature which follows last in last out (LILO/FIFO) principle
'''

class QueueUsingList:
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


if __name__ == "__main__":
    queue_using_list = QueueUsingList()
    queue_using_list.enqueue(10)
    queue_using_list.enqueue(20)
    queue_using_list.enqueue(30)
    queue_using_list.enqueue(40)
    print(queue_using_list.dequeue())
    print(queue_using_list.get_rear())
    print(queue_using_list.get_first())