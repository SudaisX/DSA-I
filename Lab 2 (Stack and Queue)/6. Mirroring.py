import ast
queue = input()
queue = ast.literal_eval(queue)

class Stack:
    def __init__(self):
        self.stack = []   
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def is_empty(self):
        return self.stack == []

class Queue:
    def __init__(self):
        self.queue = []    
    def enQueue(self, item):
        self.queue.append(item)
    def deQueue(self):
        return self.queue.pop(0)
    def is_empty(self):
        return self.queue == []

def mirror(lst):
    q, s = Queue(), Stack()
    q.queue = lst #the input queue
    
    while len(q.queue) != len(s.stack):
        x = q.deQueue()
        s.push(x) #stacking the popped values
        q.enQueue(x) #adding the popped values back to the queue too

    while not(s.is_empty()):
        q.enQueue(s.pop())
    return q.queue

print(mirror(queue))