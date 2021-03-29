from random import randint

def quicksort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        
        less = [i for i in lst[1:] if i <= pivot]
        greater = [i for i in lst[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 14, 43, 2, 43, 5, 4, 19, 9]))
