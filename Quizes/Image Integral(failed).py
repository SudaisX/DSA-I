image = [[1, 0, 0, 1, 0],
         [0, 0, 0, 1, 0], 
         [0, 1, 0, 1, 0], 
         [1, 1, 0, 1, 0], 
         [1, 0, 0, 1, 1]]

def integral_image(image):
    size = len(image)
    integral = [[0 for col in range(size)] for row in range(size)]

    for row in range(size):
        for col in range(size):
            if col == 0 and row == 0:
                integral[row][col] = image[row][col]
            elif col > 0 and row == 0:
                integral[row][col] = image[row][col] + sum([image[row][i] for i in range(col)])
            elif col > 0 and row > 0:
                total = 0
                for r in range(row):
                    total += sum([image[r][c] for c in range(col)])
                integral[row][col] = image[row][col] + sum([image[i][col] for i in range(row)]) + total
    return integral
    
print(integral_image(image))