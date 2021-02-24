def sum_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_digits(int(n/10))

n = int(input())

import inspect
source = inspect.getsource(sum_digits)
if '[' in source:
  print('Do not convert to string!')
elif 'for' in source or 'while' in source:
  print('Try to solve the problem recursively!')
else:
  print(sum_digits(n))