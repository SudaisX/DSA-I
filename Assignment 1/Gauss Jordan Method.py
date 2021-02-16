import ast
coeffs = input()
coeffs = ast.literal_eval(coeffs)

def multiply_row(row, n):
    return [element*n for element in row]
def add_row(row, n):
    return [element+n for element in row]
def add_rows(row1, row2):
    return [row1[i]+row2[i] for i in range(len(row1))]

def Solve(coeffs):
    length  = len(coeffs)
    #swap until the first element is not 0
    while coeffs[0][0] == 0:
        coeffs.append(coeffs.pop(0))
            
    for i in range(length):
        #turn the pivot into 1
        if coeffs[i][i] != 1:
            try:
                coeffs[i] = multiply_row(coeffs[i], 1/coeffs[i][i])
            except ZeroDivisionError:
                coeffs[i] = add_row(coeffs[i], 1)

        #turn the rows below the pivot into 0
        for j in range(i+1, length):
            if coeffs[j][i] != 0:
                coeffs[j] = add_rows(coeffs[j], multiply_row(coeffs[i], -coeffs[j][i]))

        #turn the rows above the pivot into 0
        for j in range(i):
            if coeffs[j][i] != 0:
                coeffs[j] = add_rows(coeffs[j], multiply_row(coeffs[i], -coeffs[j][i]))
                    
    return [round(x[-1], 1) for x in coeffs] 
   
print(Solve(coeffs))