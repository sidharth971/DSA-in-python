class Node:
    def __init__(self, item=None, next=None, prev=None):
        self.item = item
        self.next = next
        self.prev = prev


class CDLL:
    def __init__(self):
        self.start = None

    def is_empty(self):
        return self.start is None

    def insert_at_first(self, val):
        node = Node(val)
        if self.is_empty():
            node.next = node
            node.prev = node
            self.start = node
        else:
            node.prev = self.start.prev
            node.next = self.start
            self.start.prev.next = node
            self.start = node

    def insert_at_last(self, val):
        if self.is_empty():
            self.insert_at_first(val)
        else:
            node = Node(val)
            node.prev = self.start.prev.prev
            node.next = self.start
            self.start.prev = node
            if self.start.next == self.start:
                self.start.next = node

    def delete(self, val):
        temp = self.start
        while temp.next != self.start:
            if self.start.item == val:
                self.start.prev.next = self.start.next
                self.start = self.start.next
            if temp.next.item == val:
                temp.next = temp.next.next
                temp.next.next.prev = temp
                break
            temp = temp.next
        else:
            print('No data found')

    def display(self):
        if not self.is_empty():
            temp = self.start
            while temp.next != self.start:
                print(temp.item)
                temp = temp.next
            else:
                print(temp.item)
        else:
            print('No Data found')

    def __iter__(self):
        return CDLLIter(self.start)


class CDLLIter:
    def __init__(self, val):
        self.current = val
        self.first = val
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current:
            if self.current.next != self.first and self.count:
                val = self.count.item
                self.current = self.current.next
                return val
            if self.current.next == self.first:
                self.count += 1

        else:
            raise StopIteration


cdll_obj = CDLL()
cdll_obj.insert_at_last(10)
cdll_obj.insert_at_last(20)
cdll_obj.insert_at_last(40)
cdll_obj.insert_at_first(30)
cdll_obj.delete(10)
cdll_obj.display()

# for x in cdll_obj:
#     print(x)
