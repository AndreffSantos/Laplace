from random import randrange

M1 = [1] # Determinante = 1
M2 = [[2, 3], [1, 4]] # Determinante = 5
M3 = [[3, 1, 0], [-2, 2, 3], [0, 1, 2]] # Determinante = 7

def set_matrix(n: int):
    return [[randrange(5) for coloumn in range(n)] for line in range(n)]

def det(matrix: list):
    if len(matrix) == 1:
        return matrix[0]
    
    determinant = 0
    first_line = matrix[0]
    for colomn in range(len(first_line)):
        determinant += first_line[colomn] * cof(matrix, colomn)
    
    return determinant

def cof(matrix: list, index: int):
    i = 1
    j = index + 1
    return pow(-1, (i + j)) * det(minor(matrix, index))

def minor(matrix: list, index: int):
    if len(matrix) > 2:
        return [[matrix[line][colomn] for colomn in range(len(matrix[line])) if colomn != index] for line in range(len(matrix)) if line != 0]
    return [[matrix[line][colomn] for colomn in range(len(matrix[line])) if colomn != index][0] for line in range(len(matrix)) if line != 0]
    
print(det(M1))
print(det(M2))
print(det(M3))

M4 = set_matrix(2)
print(M4, det(M4))
M5 = set_matrix(3)
print(M5, det(M5))
M6 = set_matrix(4)
print(M6, det(M6))