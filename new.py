def f(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    if b % 2 == 0:
        return f(a*a, b//2)
    else:
        return f(a*a, b//2) * a
    
print(f(4, 3), f(2, 4))
