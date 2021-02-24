def partition_modulo_n(n, t):
    if n > 0:
        modulo = {num:[] for num in range(n)}
    else:
        modulo = {num:[] for num in range(n+1, 1)}
        
    for num in t:
        modulo[num%n].append(num)
    return modulo

from pprint import pprint
n = int(input().strip())
t = [int(i) for i in input().strip().split()]
pprint(partition_modulo_n(n, t))
pprint(t)
