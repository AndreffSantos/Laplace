from random import randrange

M1 = [1] # Determinante = 1
M2 = [[2, 3], [1, 4]] # Determinante = 5
M3 = [[3, 1, 0], [-2, 2, 3], [0, 1, 2]] # Determinante = 7

def gera_matriz_aleatoria(n: int):
    return [[randrange(5) for coloumn in range(n)] for line in range(n)]

def determinante(matriz: list):
    if len(matriz) == 1:
        return matriz[0]
    
    det = 0
    primeira_linha = matriz[0]
    for coluna in range(len(primeira_linha)):
        det += primeira_linha[coluna] * pow(-1, coluna) * determinante(matriz_de_ordem_menor(matriz, coluna))
    
    return det

def matriz_de_ordem_menor(matriz: list, index: int):
    if len(matriz) > 2:
        return [[matriz[linha][coluna] for coluna in range(len(matriz[linha])) if coluna != index] for linha in range(len(matriz)) if linha != 0]
    return [[matriz[linha][coluna] for coluna in range(len(matriz[linha])) if coluna != index][0] for linha in range(len(matriz)) if linha != 0]
    
print(determinante(M1))
print(determinante(M2))
print(determinante(M3))

M4 = gera_matriz_aleatoria(2)
print(M4, determinante(M4))
M5 = gera_matriz_aleatoria(3)
print(M5, determinante(M5))
M6 = gera_matriz_aleatoria(4)
print(M6, determinante(M6))