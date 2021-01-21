#LIFO (Last in, First Out) Structure
#Elements can only be added or removed from the top
#Linear and Sequential DS

#www.geeksforgeeks.org/stack-in-python/

class Stack:
    def __init__(self):
        self.stack = []
    
    def pop(self):
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

mystack = Stack()