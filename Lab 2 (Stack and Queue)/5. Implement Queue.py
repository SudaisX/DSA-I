class Queue:
    def __init__(self):
        self.q = []   
        
    def enQueue(self, item):
        self.q.append(item)
        
    def deQueue(self):
        return self.q.pop(0)
    
    def front(self):
        return self.q[0]
    
    def is_empty(self):
        return self.q == []