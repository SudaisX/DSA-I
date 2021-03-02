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

def sort_matrix_by_row(lst):
    for r in range(len(lst)):
        selection_sort(lst[r])
    return lst
        
print(sort_matrix_by_row(lst))