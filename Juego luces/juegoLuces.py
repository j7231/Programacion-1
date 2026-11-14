import numpy as np
cantidad = 10
while True:
    luces = np.zeros(cantidad)

    for posicion in range(cantidad):
        if np.random.randint(2) == 1:
            if posicion > 0:
                luces[posicion - 1] = 1-luces[posicion - 1]
            if posicion < cantidad - 1:
                luces[posicion + 1] = 1-luces[posicion + 1]
            luces[posicion] = 1-luces[posicion]

    
    if np.any(luces == 1):
        break

pos = np.zeros(10, dtype = np.uint8)

for i in range(10):
    pos[i] = i + 1
    
print(f"posiciones: {pos}")
print(f"Tablero inicial: {luces}")

while 1:
    print(f"Tablero actual:  {luces}")
    
    if not np.any(luces == 1):
        print("\n¡Felicidades, has ganado!")
        break

    escoger_posicion = int(input(f"Escoge una posicion del 1 al {cantidad}: "))

    while escoger_posicion < 1 or escoger_posicion > cantidad:
        escoger_posicion = int(input(f"Posición inválida. Escoge una posicion del 1 al {cantidad}: "))

    posicion = escoger_posicion - 1

    luces[posicion] = 1 - luces[posicion]

    if posicion > 0:
        luces[posicion - 1] = 1 - luces[posicion - 1]

    if posicion < cantidad - 1:
        luces[posicion + 1] = 1 - luces[posicion + 1]
        
print("Felicidades has ganado") 