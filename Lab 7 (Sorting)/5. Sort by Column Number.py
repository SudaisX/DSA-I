import ast
lst = input()
lst = ast.literal_eval(lst)
column = int(input())
 
def sort_matrix_by_columnNumber(lst, column):
    for i in range(len(lst)):
        minimum = i
        for j in range(i, len(lst)):
            if lst[j][column] < lst[minimum][column]:
                minimum = j
        lst[i], lst[minimum] = lst[minimum], lst[i]
    return lst

print(sort_matrix_by_columnNumber(lst, column))