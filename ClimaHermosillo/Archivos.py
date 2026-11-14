import numpy as np
import matplotlib.pyplot as plt

def cargar_datos(nombre_archivo):
    with open(nombre_archivo,"r",encoding="utf-8") as archivo:
        datos = np.loadtxt(archivo,delimiter=",",skiprows=1)
    
    print(datos.shape)
    print(datos)
#--------------------------------

def graficar_clima(archivo):
    dias, temperaturas, radiaciones = np.loadtxt(archivo, delimiter=',', unpack=True)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.hist(temperaturas, bins=8, color="coral", edgecolor="black")
    ax1.set_title("Distribucion de Temperatura")
    ax1.set_xlabel("Temperatura (°C)")
    ax1.set_ylabel("Frecuencia (Días)")
    ax1.grid(True, linestyle="--", alpha=0.6)

    ax2.hist(radiaciones, bins=8, color="steelblue", edgecolor="black")
    ax2.set_title("Distribucion de Radiacion Solar")
    ax2.set_xlabel("Radiacion (W/m²)")
    ax2.set_ylabel("Frecuencia (Días)")
    ax2.grid(True, linestyle="--", alpha=0.6)

    plt.tight_layout()
    plt.show()
#---------------------------------

def analizar_clima():
    _, temperaturas, radiaciones = np.loadtxt(archivo, delimiter=',', unpack=True)
    
    print("\nResume del clima")
    print(f"Temperatura Promedio: {np.mean(temperaturas):.2f} °C")
    print(f"Temperatura Maxima: {np.max(temperaturas):.2f} °C")
    print(f"Temperatura Minima: {np.min(temperaturas):.2f} °C")
    print("-" * 45)
    print(f"Radiacion Promedio: {np.mean(radiaciones):.2f} W/m²")
    print(f"Radiacion Maxima: {np.max(radiaciones):.2f} W/m²")
    print(f"Radiacion Minima: {np.min(radiaciones):.2f} W/m²")
#---------------------------------

if __name__ == "__main__":
    opciones = ["Cargar datos","Graficar clima","Analizar clima"]

    for i in range(3):
        print(f"{i+1}.{opciones[i]}")

    eleccion = int(input("escoge una de las opciones anteriores[1,2,3]: "))
    archivo = "datos_de_clima_hermosillo_ultimos_50_dias.txt"
    print("\033[2J\033[H", end="")

    match eleccion:
        case 1:
            cargar_datos(archivo)
        case 2:
            graficar_clima(archivo)
        case 3:
            print(analizar_clima())

