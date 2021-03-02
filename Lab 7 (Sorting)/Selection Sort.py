import ast
lst = input()
lst = ast.literal_eval(lst)

def selection_sort(lst):
    for i in range(len(lst)):
        minimum = i
        for j in range(i, len(lst)):
            if lst[j] < lst[minimum]:
                minimum = j
        lst[i], lst[minimum] = lst[minimum], lst[i]
        print(lst)
  
selection_sort(lst)