import ast
A = input()
A = ast.literal_eval(A)

def blur_image(A):
    row_l, col_l = len(A), len(A[0])
    
    B = [[0 for i in range(col_l)] for j in range(row_l)]
    for row in range(row_l):
        for col in range(col_l):

            if row == 0 and col == 0:
                B[row][col] = round((A[row][col] + A[row+1][col] + A[row][col+1]) / 3, 2)
            elif row == 0 and col > 0 and col < (col_l-1):
                B[row][col] = round((A[row][col] + A[row][col-1] + A[row+1][col] + A[row][col+1])/4, 2)
            elif row == 0 and col == (col_l-1):
                B[row][col] = round((A[row][col] + A[row+1][col] + A[row][col-1]) / 3, 2)
            elif row > 0 and row < row_l-1 and col == 0:
                B[row][col] = round((A[row][col] + A[row+1][col] + A[row-1][col] + A[row][col+1]) / 4, 2)
            elif row > 0 and row < row_l-1 and col > 0 and col < col_l-1:
                B[row][col] = round((A[row][col] + A[row][col-1] + A[row+1][col] + A[row-1][col] + A[row][col+1])/5, 2)
            elif row > 0 and row < row_l-1 and col == col_l-1:
                B[row][col] = round((A[row][col] + A[row+1][col] + A[row-1][col] + A[row][col-1]) / 4, 2)
            elif row == row_l-1 and col == 0:
                B[row][col] = round((A[row][col] + A[row-1][col] + A[row][col+1]) / 3, 2)
            elif row == row_l-1 and col > 0 and col < (col_l-1):
                B[row][col] = round((A[row][col] + A[row][col-1] + A[row-1][col] + A[row][col+1])/4, 2)
            elif row == row_l-1 and col == col_l-1:
                B[row][col] = round((A[row][col] + A[row-1][col] + A[row][col-1]) / 3, 2)
    
    return B

print(blur_image(A))