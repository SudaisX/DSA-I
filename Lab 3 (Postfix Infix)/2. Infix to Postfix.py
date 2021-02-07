expression = input()
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
    

def Infix_to_Postfix(expression):
    op_stack = Stack()
    operators = ['+', '-', '*', '/']
    precedence = {'+':1, '-':1, '*':2, '/':2}
    output = []
    
    
    for n in expression.split():
        if n.isnumeric():
            output.append(n)
        elif n == '(':
            op_stack.push(n)
        elif n == ')':
            while op_stack.top() != '(':
                output.append(op_stack.pop())
            op_stack.pop()
        elif n in operators:
            while not(op_stack.is_empty()) and op_stack.top() != '(' and precedence[op_stack.top()] >= precedence[n]:
                output.append(n)
            op_stack.push(n)
            
    while not(op_stack.is_empty()):
        output.append(op_stack.pop())
        
    return ''.join(output)

print(Infix_to_Postfix(expression))