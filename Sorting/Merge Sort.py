def mergeSort(arr):
    if len(arr) < 2:
        return arr
    else:
        a = arr[:len(arr)//2]
        b = arr[len(arr)//2:]

        a = mergeSort(a)
        b = mergeSort(b)
        c = []

        i = 0
        j = 0

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i = i + 1
            else:
                c.append(b[j])
                j = j + 1
                
        c += a[i:]
        c += b[j:]
    return c

testList = [1,3,5,7,2,6,25,18,13]
print(mergeSort(testList))

# def merge(left, right):
#     result = []
#     i,j = 0,0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result

# def merge_sort(lst):
#     if len(lst) < 2:
#         return lst
#     else:
#         middle = len(lst)//2
#         left = merge_sort(lst[:middle])
#         right = merge_sort(lst[middle:])
#         return merge(left, right)
        


#print(merge_sort(testList))

# def mergeSort(lst, ascending=True):
#     if len(lst) < 2:
#         return lst
        
#     middle = len(lst)//2
#     left = mergeSort(lst[:middle], ascending)
#     right = mergeSort(lst[middle:], ascending)

#     result = []
#     i,j = 0,0
#     while i < len(left) and j < len(right):
#         if (left[i] < right[j] and ascending) or (left[i] > right[j] and not(ascending)):
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result

# def mergeSort(lst):
#     if len(lst) < 2:
#         return lst
        
#     middle = len(lst)//2
#     left = mergeSort(lst[:middle])
#     right = mergeSort(lst[middle:])

#     result = []
#     i,j = 0,0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result

arr2 = [2, 4, 1, 3, 5]
arr = [1, 20, 6, 4, 5]
#print(mergeSort(arr2))