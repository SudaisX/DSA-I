s=input()

class Stack:
    def __init__(self):
        self.stack = []   
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def is_empty(self):
        return self.stack == []

def balanced_braces(string):
    stack = Stack()
    braces_open = ['(', '[', '{',]
    braces_close = [')', ']', '}',]
    
    for s in string:
        if s in braces_open:
            stack.push(s)
        elif s in braces_close:
            i = braces_close.index(s)
            if not(stack.is_empty()) and braces_open[i] in stack.stack:
                stack.pop()
            else:
                return False  
    return stack.is_empty()
    
print(balanced_braces(s))