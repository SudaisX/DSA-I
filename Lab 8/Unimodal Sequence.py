unimodel_sequence = input().split(" ")
unimodel_sequence = [int(i) for i in unimodel_sequence]

def getTopIndex_UnimodelSequence(unimodel_sequence):
    low, high = 0, len(unimodel_sequence)-1

    while low < high:
        mid = (low+high) // 2
        if unimodel_sequence[mid] < unimodel_sequence[mid+1]:
            low = mid + 1 
        else:
            unimodel_sequence[mid] > unimodel_sequence[mid+1]
            high = mid
    return low

print(getTopIndex_UnimodelSequence(unimodel_sequence))