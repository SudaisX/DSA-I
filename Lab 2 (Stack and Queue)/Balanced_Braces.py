class Stack:
    def __init__(self):
        self.stack = []   
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def is_empty(self):
        return self.stack == []
    def top(self):
        return self.stack[-1]

def balanced_braces(string):
    stack = Stack()
    for s in string:
        if s == '{': stack.push('}')
        elif s == '[': stack.push(']')
        elif s == '(': stack.push(')')
        else:
            if stack.is_empty() or stack.top() != s:
                return False
            else:
                stack.pop()
    return stack.is_empty()

string = input('Enter braces: ')
print(balanced_braces(string))