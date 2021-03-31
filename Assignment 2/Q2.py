def CountInversions(lst):
    def MergeSortandCountInversions(lst) :
        if len(lst) < 2:
            return lst, 0
            
        mid = len(lst)//2
        left, left_i = MergeSortandCountInversions(lst[:mid])
        right, right_i = MergeSortandCountInversions(lst[mid:])
        
        result = []
        i, j = 0, 0
        inversions = left_i + right_i
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                inversions += (mid - i)

        result += left[i:]
        result += right[j:]
        return result, inversions
    return MergeSortandCountInversions(lst)[1]

arr = [2, 4, 1, 3, 5]
print(CountInversions(arr))