from random import randint

def quickSort(lst, ascending=True):
    if len(lst) < 2:
        return lst
    else:
        r = len(lst)
        pivot = randint(0, r-1)

        if ascending:
            left = [lst[i] for i in range(r) if lst[i] <= lst[pivot] and i != pivot]
            right = [lst[i] for i in range(r) if lst[i] > lst[pivot] and i != pivot]
        else:
            left = [lst[i] for i in range(r) if lst[i] > lst[pivot] and i != pivot]
            right = [lst[i] for i in range(r) if lst[i] <= lst[pivot] and i != pivot]

        return quickSort(left, ascending) + [lst[pivot]] + quickSort(right, ascending)

print(quickSort([10, 14, 43, 2, 43, 5, 4, 19, 9]))