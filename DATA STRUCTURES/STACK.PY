class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):  # Renamed from insEmpty to isEmpty
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def peek(self):
        if self.isEmpty():  # Corrected to call isEmpty from the class
            print("No element to peek from stack")
            return None
        return self.stack[-1]

    def push(self, item):  # Renamed parameter from int to item
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():  # Corrected to call isEmpty from the class
            print("No element to pop from stack")
            return None
        return self.stack.pop()


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(60)

while not s.isEmpty():
    print(s.peek())
    s.pop()
