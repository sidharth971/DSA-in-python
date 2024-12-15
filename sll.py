'''
@Sidharth Sahoo
Single Link List: It is a linear data strature where elements are store in contiguous memory location.
                  Every element called as Node.
'''


class Node:
    def __init__(self, val=None, next=None):
        self.item = val
        self.next = next


class SLL:
    def __init__(self):
        self.head = None

    def insert_at_first(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            temp = self.head
            self.head = node
            self.head.next = temp

    def insert_at_last(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            temp = self.head
            while temp:
                if not temp.next:
                    temp.next = node
                temp = temp.next

    def insert_at_index(self, val, index):
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            temp = self.head
            count = 0
            while temp.next or count <= index:
                if count == index or not temp.next:
                    temp.next = node
                temp = temp.next
                count += 1

    def search(self, val):
        temp = self.head
        while temp:
            if temp.item == val:
                print(temp.item)
                break
            temp = temp.next
        else:
            print('No match found')

    def delete(self, val):
        if self.head:
            if self.head.item == val:
                if self.head.next:
                    self.head = self.head.next
                else:
                    self.head = None
            temp = self.head
            while temp.next:
                if temp.next.item == val:
                    temp.next = temp.next.next
                    break
                temp = temp.next
            else:
                print('Not fount in list')
        else:
            print('List is empty')

    def display(self):
        if self.head:
            temp = self.head
            while temp:
                print(temp.item)
                temp = temp.next
        else:
            print('No data found')

    def __iter__(self):
        return Iterable(self.head)


class Iterable:
    '''
    Create custum iterator
    '''

    def __init__(self, value):
        self.current = value

    def __iter__(self):
        return self

    def __next__(self):
        if self.current:
            value = self.current.item
            self.current = self.current.next
            return value
        else:
            raise StopIteration


sll_obj = SLL()
sll_obj.insert_at_last(20)
sll_obj.insert_at_first(10)
# sll_obj.search(20)
sll_obj.insert_at_index(30, 1)
# sll_obj.display()
# for x in sll_obj:
#     print(x)

sll_obj.delete(10)

sll_obj.display()