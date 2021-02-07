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

def EvalutePrefix(expression):
    operandStack = Stack()
    
    operands = ['*', '/', '+', '-']
    
    for n in expression[::-1].split():
        if n in operands:
            n1, n2 = operandStack.pop(), operandStack.pop()
            operandStack.push(int(eval(f'{n1}{n}{n2}')))
        else:
            operandStack.push(int(n))
    
    return(operandStack.top())
        
        
expression = input()
print(EvalutePrefix(expression))