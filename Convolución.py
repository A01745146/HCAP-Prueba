import numpy as np

M = [[1,2,3,4,5,6],[7,8,9,10,11,12],[0,0,1,16,17,18],[0,1,0,7,23,24],[1,7,6,5,4,3]]
filtro = [[1,1,1],[0,0,0],[2,10,3]]


def convolucion(A, B):
    filas = (len(A)-len(B))+1
    columnas = (len(A[0])-len(B[0]))+1
    C = np.zeros((filas, columnas))
    i=0
    k=0
    result = 0
    for x in range(len(C)):
        for w in range(len(C[0])):
            for y in range(len(B)):
                for z in range(len(B[y])):
                    result += A[y+i][z+k]*B[y][z]
            C[x][w] += result
            result = 0
            k += 1
        i += 1
        k = 0
    C = np.array(C)
    return C

print(convolucion(M, filtro))