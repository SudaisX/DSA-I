import ast
InputString = input()
G = int(input())

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
    
#Version 2        
def Verify(InputString, grammerIndex):
    PDA = Stack()
    def verify(PDA, InputString, grammerIndex, dual_pop, a, b, c, d):
        popped = False
        popped2 = False
        for s in InputString:
            if s == a:
                if not(popped): PDA.push(a)
                else: return False
            elif s == b: 
                if not(PDA.is_empty()): 
                    PDA.pop()
                    popped = True
                    if dual_pop:
                        if not(PDA.is_empty()): PDA.pop()
                        else: return False
                else: return False
            elif s == c and not(popped2): PDA.push(c)
            elif s == d:
                if not(PDA.is_empty()) and PDA.top() == c: 
                    PDA.pop()
                    popped2 = True
                else: return False
            
        if grammerIndex == 1 or grammerIndex == 2:
            if PDA.is_empty(): return True
            else: return False
        elif grammerIndex == 3:
            if PDA.is_empty() and popped and popped2: return True
            else: return False  
        elif grammerIndex == 4:
            if PDA.is_empty() or not(popped): return False
            else: return True
        
    if grammerIndex == 1:
        return verify(PDA, InputString, grammerIndex, False, '1', '0', '', '')
    elif grammerIndex == 2:
        return verify(PDA, InputString, grammerIndex, True, '1', '0', '', '')  
    elif grammerIndex == 3:
        return verify(PDA, InputString, grammerIndex, False, '0', '1', '2', '3')
    elif grammerIndex == 4:
        return verify(PDA, InputString, grammerIndex, False, '0', '1', '', '')

print(Verify(InputString, G))