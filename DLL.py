'''
@Sidharth Sahoo
Double Link List: It is the linear data stature which holds heterogeneous element.
DLL is the collection of nodes which has two way link.
'''


class Node:
    def __init__(self, item=None, next=None, previous=None):
        self.item = item
        self.next = next
        self.previous = previous


class DLL:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_first(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            temp = self.head
            node.next = temp
            self.head = node

    def insert_at_last(self, val):
        node = Node(val)
        if not self.head:
            self.insert_at_first(val)
        else:
            temp = self.head
            while temp:
                if not temp.next:
                    temp.next = node
                    node.previous = temp
                    break
                temp = temp.next

    def delete(self, val):
        if self.head:
            if self.head.item == val:
                self.head = self.head.next
            else:
                temp = prev = self.head
                while temp:
                    if temp.item == val:
                        prev.next = temp.next
                        temp.next.previous = prev
                        break
                    prev = temp
                    temp = temp.next

                else:
                    print('No data found')
        else:
            print('No data in DLL')

    def search_index(self, val):
        temp = self.head
        count = 0
        while temp:
            if temp.item == val:
                return count
            count += 1
            temp = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.item)
            temp = temp.next

    def __iter__(self):
        return IteratorDLL(self.head)


class IteratorDLL:
    def __init__(self, val):
        self.current = val
    def __iter__(self):
        return self
    def __next__(self):
        if self.current:
            value = self.current.item
            self.current = self.current.next
            return value
        else:
            raise StopIteration


dll_obj = DLL()
dll_obj.insert_at_last(20)
dll_obj.insert_at_last(40)
dll_obj.insert_at_first(10)
dll_obj.insert_at_first(30)
print(dll_obj.search_index(30))
dll_obj.delete(30)
# dll_obj.display()
for x in dll_obj:
    print(x)
