s = input()

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def is_empty(self):
        return self.stack == []
    
def string_reversal(string):
    stack = Stack()
    for s in string:
        stack.push(s)
    string = ''
    while not(stack.is_empty()):
        string += stack.pop()
    return string

print(string_reversal(s))