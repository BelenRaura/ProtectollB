import numpy as np
import matplotlib.pyplot as plt

def calcular_fractal(x_min, x_max, y_min, y_max, ancho, alto, iteraciones_max):
    # Crear una cuadrícula de puntos complejos en el plano
    x = np.linspace(x_min, x_max, ancho)
    y = np.linspace(y_min, y_max, alto)
    X, Y = np.meshgrid(x, y)
    c = X + 1j * Y
    
    # Inicializar el arreglo de iteraciones y la variable z
    z = np.zeros(c.shape, dtype=complex)
    iteraciones = np.zeros(c.shape, dtype=int)

    # Iterar la ecuación del fractal
    for i in range(iteraciones_max):
        mascara = np.abs(z) <= 2
        z[mascara] = z[mascara]**2 + c[mascara]
        iteraciones[mascara] += 1

    # Regresar el número de iteraciones antes de diverger
    return iteraciones

def visualizar_fractal(iteraciones, x_min, x_max, y_min, y_max):
    plt.figure(figsize=(10, 10))
    plt.imshow(iteraciones, extent=(x_min, x_max, y_min, y_max), cmap='hot')
    plt.colorbar(label='Número de iteraciones')
    plt.title('Fractal en el plano complejo')
    plt.xlabel('Re(c)')
    plt.ylabel('Im(c)')
    plt.show()

# Parámetros iniciales
x_min, x_max = -2.25, 1.25
y_min, y_max = -1.5, 1.5
ancho, alto = 1000, 1000
iteraciones_max = 100

# Calcular y visualizar el fractal
iteraciones = calcular_fractal(x_min, x_max, y_min, y_max, ancho, alto, iteraciones_max)
visualizar_fractal(iteraciones, x_min, x_max, y_min, y_max)
