'''
@Sidharth Sahoo
Circle Link List: It is the linear data stature which holds heterogeneous element.
CLL is the collection of nodes which has last node link to first node.
'''


class Node:
    def __init__(self, item=None, next=None, tail=None):
        self.item = item
        self.next = next


class CLL:
    def __init__(self):
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_at_first(self, val):
        node = Node(val)
        if self.tail:
            node.next = self.tail.next
            self.tail.next = node
        else:
            self.tail = node
            self.tail.next = node

    def insert_at_last(self, val):
        node = Node(val)
        node.next = self.tail.next
        self.tail.next = node
        self.tail = node

    def delete(self, val):
        temp = self.tail.next
        while temp:
            if self.tail.item == val:
                temp = self.tail.next
                while temp.next != self.tail:
                    temp = temp.next
                else:
                    temp.next = self.tail.next
                    self.tail = temp
                    break
            if self.tail.next.item == val:
                self.tail.next = self.tail.next.next
                break
            if temp.next.item == val:
                temp.next = temp.next.next
                break
            temp = temp.next
        else:
            print('No data found!')

    def display(self):
        temp = self.tail.next
        while temp.next != self.tail.next:
            print(temp.item)
            temp = temp.next
        else:
            print(temp.item)

    def __iter__(self):
        return CLLIterator(self.tail.next)


class CLLIterator:
    def __init__(self, val):
        self.current = val
        self.temp = val
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        if self.current:
            if self.current == self.temp  and self.count:
                raise StopIteration
            else:
                self.count +=1
            value = self.current.item
            self.current = self.current.next
            return value
        else:
            raise StopIteration


cll_obj = CLL()
cll_obj.insert_at_first(10)
cll_obj.insert_at_first(20)
cll_obj.insert_at_last(30)
cll_obj.insert_at_last(40)
cll_obj.delete(20)
# cll_obj.display()

for x in cll_obj:
    print(x)
