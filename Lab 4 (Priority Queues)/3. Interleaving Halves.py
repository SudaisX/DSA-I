import ast
lst = input()
lst = ast.literal_eval(lst)

class Stack:
    def __init__(self):
        self.stack = [] 
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def top(self):
        return self.stack[-1]
    def is_empty(self):
        return self.stack == []

class Queue:
    def __init__(self):
        self.queue = []   
    def enQueue(self, item):
        self.queue.append(item) 
    def deQueue(self):
        return self.queue.pop(0)
    def front(self):
        return self.queue[0]
    def is_empty(self):
        return self.queue == []

def InterLeaveQueue(lst):
    integers = Queue()
    integers.queue = lst
    temp, half = Stack(), Stack()  
    
    while len(temp.stack) != len(integers.queue):
        temp.push(integers.deQueue())
        
    while not(temp.is_empty()):
        half.push(temp.pop())
    
    while not(half.is_empty()):
        integers.enQueue(half.pop())
        integers.enQueue(integers.deQueue())

    return integers.queue

print(InterLeaveQueue(lst))