def matrix_transpose(A):
    result = [[0 for i in range(len(A))] for j in range(len(A[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[j][i] = A[i][j]
    return result
            
print(matrix_transpose(A))