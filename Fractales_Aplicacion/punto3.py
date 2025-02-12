import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

# Parámetros iniciales de la imagen
width, height = 800, 800
x_min, x_max = -1.5, 1.5
y_min, y_max = -1.2, 1.2
max_iter = 180  # Número máximo de iteraciones

# Definir un valor fijo para C
C_fixed = complex(0.28, 0.53)

# Función para calcular el conjunto de Julia
def compute_julia_set(x_min, x_max, y_min, y_max, width, height, max_iter, C_fixed):
    x_values = np.linspace(x_min, x_max, width)
    y_values = np.linspace(y_min, y_max, height)
    julia_set = np.zeros((height, width))

    for i, y in enumerate(y_values):
        for j, x in enumerate(x_values):
            Z = complex(x, y)  # Cada punto en la cuadrícula
            C = C_fixed  # Se usa el mismo C en todas las iteraciones
            iter_count = 0
            while abs(Z) <= 2 and iter_count < max_iter:
                Z = Z**2 + C
                iter_count += 1
            julia_set[i, j] = iter_count

    return julia_set

# Función para redibujar la imagen con nuevos límites
def redraw_julia_set(x_min, x_max, y_min, y_max):
    # Calcular el nuevo conjunto de Julia
    julia_set = compute_julia_set(x_min, x_max, y_min, y_max, width, height, max_iter, C_fixed)

    # Actualizar la imagen
    im.set_data(julia_set)
    im.set_extent([x_min, x_max, y_min, y_max])

    # Actualizar los límites de los ejes
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

    # Redibujar las iteraciones
    for scatter in ax.collections:
        scatter.remove()  # Eliminar los puntos anteriores
    for text in ax.texts:
        text.remove()  # Eliminar los textos anteriores

    # Agregar las primeras 8 iteraciones como puntos blancos (sin etiquetas de iteración)
    for i, (x, y) in enumerate(iterations[:-1]):
        if x_min <= x <= x_max and y_min <= y <= y_max:  # Asegurar que esté dentro del área de la imagen
            ax.scatter(x, y, color='white', marker='o', s=30)  # Eliminado el parámetro `label`
            ax.text(x, y, f'P{i} ({x:.2f}, {y:.2f})', fontsize=12, color='white', ha='right', va='bottom')

    # Eliminar la tabla si existe
    global table
    if table is not None:
        table.remove()
        table = None

    # Redibujar la figura
    plt.draw()

# Función para manejar el evento de zoom con el mouse
def on_press(event):
    global x_min, x_max, y_min, y_max
    if event.button == 1:  # Botón izquierdo del ratón (zoom hacia adentro)
        x_center, y_center = event.xdata, event.ydata
        if x_center is not None and y_center is not None:
            # Calcular nuevos límites para hacer zoom hacia adentro
            zoom_factor = 0.5  # Factor de zoom (ajustable)
            x_range = (x_max - x_min) * zoom_factor
            y_range = (y_max - y_min) * zoom_factor
            x_min, x_max = x_center - x_range / 2, x_center + x_range / 2
            y_min, y_max = y_center - y_range / 2, y_center + y_range / 2
            redraw_julia_set(x_min, x_max, y_min, y_max)

    elif event.button == 3:  # Botón derecho del ratón (zoom hacia afuera)
        x_center, y_center = event.xdata, event.ydata
        if x_center is not None and y_center is not None:
            # Calcular nuevos límites para hacer zoom hacia afuera
            zoom_factor = 2.0  # Factor de zoom (ajustable)
            x_range = (x_max - x_min) * zoom_factor
            y_range = (y_max - y_min) * zoom_factor
            x_min, x_max = x_center - x_range / 2, x_center + x_range / 2
            y_min, y_max = y_center - y_range / 2, y_center + y_range / 2
            redraw_julia_set(x_min, x_max, y_min, y_max)

# Calcular las primeras 8 iteraciones de Z_n para C_fixed
C = C_fixed
Z = complex(0, 0)  # Z0
iterations = [(Z.real, Z.imag)]  # Lista para almacenar las coordenadas de las iteraciones
for i in range(4):
    Z = Z**2 + C
    iterations.append((Z.real, Z.imag))

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(40, 40))  # Tamaño constante de la figura
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

# Dibujar el conjunto de Julia inicial
julia_set = compute_julia_set(x_min, x_max, y_min, y_max, width, height, max_iter, C_fixed)
im = ax.imshow(julia_set, extent=[x_min, x_max, y_min, y_max], cmap='viridis', norm=LogNorm(vmin=1, vmax=julia_set.max()), origin='lower')

# Agregar las primeras 8 iteraciones como puntos blancos (sin etiquetas de iteración)
for i, (x, y) in enumerate(iterations[:-1]):
    if x_min <= x <= x_max and y_min <= y <= y_max:  # Asegurar que esté dentro del área de la imagen
        ax.scatter(x, y, color='white', marker='o', s=30)  # Eliminado el parámetro `label`
        ax.text(x, y, f'P{i} ({x:.2f}, {y:.2f})', fontsize=15, color='black', ha='right', va='bottom')

# Agregar cuadrícula y ejes cartesianos
ax.axhline(0, color='white', linewidth=1.2)  # Eje X
ax.axvline(0, color='white', linewidth=1.2)  # Eje Y
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.6)  # Cuadrícula

# Establecer marcas en los ejes cada 0.1 unidades
ax.set_xticks(np.arange(x_min, x_max + 0.1, 0.1))
ax.set_yticks(np.arange(y_min, y_max + 0.1, 0.1))

# Etiquetas
ax.set_title(f"Conjunto de Julia con C = {C_fixed}")
ax.set_xlabel("Re(Z)")
ax.set_ylabel("Im(Z)")

# Crear una tabla con las iteraciones
col_labels = ["Iteración", "Re(Z)", "Im(Z)"]
table_data = [(f'P{i}', f'{x:.4f}', f'{y:.4f}') for i, (x, y) in enumerate(iterations)]
table = ax.table(cellText=table_data, colLabels=col_labels, cellLoc='center', loc='upper right', bbox=[0.65, 0.6, 0.3, 0.3])
table.auto_set_font_size(False)
table.set_fontsize(10)

# Conectar el evento de clic del ratón
fig.canvas.mpl_connect('button_press_event', on_press)

# Mostrar la gráfica
plt.show()