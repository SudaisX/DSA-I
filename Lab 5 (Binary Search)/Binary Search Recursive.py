import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())
low = int(input())
high = int(input())

def binary_search_recursive(lst, item, low, high):
    if high < low:
        return -1
    else:
        mid = (high+low) // 2
        if item == lst[mid]:
            return mid
        elif item > lst[mid]:
            return binary_search_recursive(lst, item, mid+1, high)
        else:
            return binary_search_recursive(lst, item, low, high-1)

print(binary_search_recursive(lst, item, low, high))