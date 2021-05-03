def printMove(fr, to):
    print(f'move from {str(fr)} to {str(to)}')

def Towers(n, fr, to, spare):
    if n == 1:
        print(f'move from {str(fr)} to {str(to)}')
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
    
Towers(3, 'old tower', 'new tower', 'spare tower')