M1 = [1] # Determinante = 1
M2 = [[2, 3], [1, 4]] # Determinante = 5

def det(matrix: list):
    if len(matrix) == 1:
        return matrix[0]
    
    determinant = 0
    line = matrix[0]
    for colomn in range(len(line)):
        determinant += line[colomn] * cof(matrix, colomn)
    
    return determinant

def cof(matrix: list, index: int):
    i = 1
    j = index + 1
    return pow(-1, (i + j)) * det(minor(matrix, index))

def minor(matrix: list, index: int):
    new_matrix = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i and j != index:
                new_matrix.append(matrix[i][j])

    return new_matrix
    
print(det(M1))
print(det(M2))