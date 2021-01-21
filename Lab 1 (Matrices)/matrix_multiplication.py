def matrix_multiplication(A, B):
    Arow, Acol = len(A), len(A[0])
    Brow, Bcol = len(B), len(B[0])
    #print(Arow, Acol, Brow, Bcol)
    
    def multiply(x, y):
        result = [[0 for i in range(y)] for j in range(x)]
        #print(result)
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    pass
                    result[i][j] += A[i][k] * B[k][j]
        return result
    
    if Arow == Bcol:
        return multiply(Arow, Bcol)
    
    elif Acol == Brow:
        return multiply(Arow, Bcol)
    else:
        return 'The number of columns in Matrix A does not equal the number of rows in Matrix B required for Matrix Multiplication.'
    
print(matrix_multiplication(A,B))