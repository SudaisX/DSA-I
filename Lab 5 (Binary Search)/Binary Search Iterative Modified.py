import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())

def binary_search_iterative_modified(lst, item):
    first = 0
    last = len(lst)-1
    while first <= last:
        mid = (first + last) // 2
        if item == lst[mid]:
            return mid
        elif item > lst[mid]:
            first = mid + 1
        else:
            last = mid - 1
    lst.insert(first, item)
    return first  

print(binary_search_iterative_modified(lst, item))