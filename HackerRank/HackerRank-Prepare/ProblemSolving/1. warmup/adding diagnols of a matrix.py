def addingDiagonals(matrix):
    diagonals = [0,0]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i==j:
                diagonals[0] += matrix[i][j]
            if i+j==2:
                diagonals[1] += matrix[i][j]
    return diagonals[0]-diagonals[1]
    # primaryDiagonal.append(matrix[i][j])
    
    
    

matrix = [[1,2,3],[4,5,6],[9,8,9]]

result = addingDiagonals(matrix)
print(result)
# print(f"the diagonal difference is: {result}")