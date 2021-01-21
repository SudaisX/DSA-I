#LIFO (Last in, First Out) Structure
#Elements can only be added or removed from the top
#Linear and Sequential DS

#Methods
#stack.push()
#stack.pop()
#stack.top()

#www.geeksforgeeks.org/stack-in-python/

class Stack:
    def __init__(self):
        self.stack = []
    
    def pop(self):
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

x = Stack()

x.stack = [1, 2, 3 , 4, 5, 6, 7, 8]

print(x.pop())