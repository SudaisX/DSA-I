class Stack:
    def __init__(self):
        stack = [] 
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def top(self):
        return self.stack[-1]
    def is_empty(self):
        return self.stack == []
    
lst = Stack()