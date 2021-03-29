import ast
lst = input()
lst = ast.literal_eval(lst)

def bubble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
        print(lst)
               
bubble_sort(lst)