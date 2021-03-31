def exercise2(N):
    count = 0
    i = N
    while i > 0:
        for j in range(0, i):
            count += 1
            print(count, j, i)
        print('-'*10)
        i = i//2

print('N = 100')
exercise2(10)