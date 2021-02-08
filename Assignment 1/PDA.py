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
    
PDA = Stack()

#CODE NEEDS OPTIMISATION #DRY (Dont Repeat Yourself)
def Verify(InputString, grammerIndex):
    popped, popped2 = False, False 
    if grammerIndex == 1:
        for s in InputString:
            if s == '1':
                if not(popped): PDA.push('1')
                else: return False
            else: 
                if not(PDA.is_empty()): 
                    PDA.pop()
                    popped = True
                else: return False
        if PDA.is_empty(): return True
        else: return False
    
    elif grammerIndex == 2:
        for s in InputString:
            if s == '1' and not(popped): PDA.push('1')
            else: 
                if not(PDA.is_empty()): 
                    popped = True
                    PDA.pop()
                    if not(PDA.is_empty()): PDA.pop()
                    else: return False
                else: return False
        if PDA.is_empty(): return True
        else: return False    

    elif grammerIndex == 3:
        for s in InputString:
            if s == '0' and not(popped): PDA.push('0')
            elif s == '1':
                if not(PDA.is_empty()) and PDA.top() == '0': 
                    PDA.pop()
                    popped = True
                else: return False
            elif s == '2' and not(popped2): PDA.push('2')
            elif s == '3':
                if not(PDA.is_empty()) and PDA.top() == '2': 
                    PDA.pop()
                    popped2 = True
                else: return False
        if PDA.is_empty() and popped and popped2: return True
        else: return False  
    
    elif grammerIndex == 4:
        for s in InputString:
            if s == '0' and not(popped): PDA.push('0')
            else: 
                if not(PDA.is_empty()): 
                    PDA.pop()
                    popped = True
                else: return False
        if PDA.is_empty() or not(popped): return False
        else: return True
print(Verify(InputString, G))