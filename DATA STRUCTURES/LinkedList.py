class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList(Node):

    def __init__(self,values = None):
        self.head  = None
        if values:
            self.head = Node(values[0])
            curr = self.head
            for value in values:
                curr.next = Node(value)
                curr = curr.next
    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next
values = [10,20,30,40,50,60,70]
l1 = LinkedList(values)
l1.display()