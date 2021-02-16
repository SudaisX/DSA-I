import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())

def binary_search_iterative(lst, item):
    first, last = 0, len(lst)

    while first <= last:
        mid = (first + last) // 2
        if item == lst[mid]:
            return mid
        elif item > lst[mid]:
            first = mid + 1
        else:
            last = mid - 1
    return -1

print(binary_search_iterative(lst, item))