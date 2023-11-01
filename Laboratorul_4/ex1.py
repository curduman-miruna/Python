class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not len(self.items) == 0:
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not len(self.items) == 0:
            return self.items[-1]
        else:
            return None

stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek())
stack.pop()
print(stack.pop())