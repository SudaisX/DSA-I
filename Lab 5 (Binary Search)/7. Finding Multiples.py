import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())

# def finding_multiple(lst, item):
#     indexes = []
#     for n in range(len(lst)):
#         if item == lst[n]:
#             indexes.append(n)
#     return indexes

def binary_search(lst, item):
    first = 0
    last = len(lst)-1
    indexes = []
    while first <= last:
        mid = (first + last) // 2
        if item == lst[mid]:
            indexes.append(mid)
            first = mid + 1
        elif item > lst[mid]:
            first = mid + 1
        else:
            last = mid - 1
    return []

print(finding_multiple(lst, item))