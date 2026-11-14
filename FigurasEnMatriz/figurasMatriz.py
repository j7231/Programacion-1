import numpy as np

def dibujo_casa():
    
    ancho = 37
    alto_techo = 10
    alto_base = 11
    alto_total = alto_techo + alto_base
    
    matriz = np.full((alto_total, ancho), ' ', dtype="U1")
    
    for i in range(alto_techo):
        matriz[i, 18 - 2 * i] = '*'
        matriz[i, 18 + 2 * i] = '*'
        
    matriz[alto_techo - 1, :] = '*'
    
    matriz[alto_techo:, 2] = '*'
    matriz[alto_techo:, ancho - 3] = '*'
    matriz[alto_total - 1, :] = '*'
    matriz[12:18, 5] = '*'
    matriz[12:18, 11] = '*'
    matriz[12, 5:12] = '*'
    matriz[17, 5:12] = '*'
    matriz[12:18, 8] = '*'   
    matriz[14, 5:12] = '*'  
    
    matriz[14:, 14] = '*'
    matriz[14:, 18] = '*'
    matriz[14, 14:19] = '*'
    
    matriz[12:18, 21] = '*'
    matriz[12:18, 27] = '*'
    matriz[12, 21:28] = '*'
    matriz[17, 21:28] = '*'
    matriz[12:18, 24] = '*' 
    matriz[14, 21:28] = '*'  

    for fila in matriz:
        print("".join(fila))

def triángulo_invertido_hueco(n):
    matriz = np.full((n, 2 * n - 1), ' ', dtype="U1")
    
    matriz[0, :] = '*'
    
    for i in range(n):
        matriz[i, i] = '*'               
        matriz[i, (2 * n - 2) - i] = '*'  
        
    for fila in matriz:
        print("".join(fila))

def triángulo_hueco(n):
    matriz = np.full((n, 2 * n - 1), ' ', dtype="U1")
    
    matriz[n - 1, :] = '*'
    
    for i in range(n):
        matriz[i, (n - 1) - i] = '*'      
        matriz[i, (n - 1) + i] = '*'      
        
    for fila in matriz:
        print("".join(fila))

def reloj_de_arena_lleno(n):
    
    filas = 2 * n - 1
    matriz = np.full((filas, 2 * n - 1), ' ', dtype="U1")
    

    for i in range(n):
        matriz[i, i : (2 * n - 1) - i] = '*'

    for i in range(n):
        matriz[filas - 1 - i, i : (2 * n - 1) - i] = '*'
        
    for fila in matriz:
        print("".join(fila))

def triangulo(n):
    
    matriz = np.full((n, 2*n-1), ' ', dtype="U1")

    for i in range(n):
        for j in range( n-i-1, n-i-1+2*i+1 ):
            matriz[i, j] = "*"
    
    for fila in matriz:
        print("".join(fila))
    
triangulo(5)
print()
triángulo_invertido_hueco(5)
print()
triángulo_hueco(5)
print()
reloj_de_arena_lleno(5)
print()
dibujo_casa()