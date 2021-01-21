def matrix_subtraction(A, B):
    
    if len(A[0]) == len(B[0]):
        return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    else:
        return "Matrices A and B don't have the same dimension required for matrix subtraction."
    
print(matrix_subtraction(A,B))