class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not len(self.items) == 0:
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not len(self.items) == 0:
            return self.items[0]
        else:
            return None

queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
print(queue.peek())
queue.pop()
print(queue.pop())