import tkinter as tk
import subprocess
from PIL import Image, ImageTk  # Necesita instalarse con `pip install pillow`
import ttkbootstrap as ttk  # Necesita instalarse con `pip install ttkbootstrap`

# Función para ejecutar un archivo .py
def ejecutar_script(script):
    subprocess.run(["python", script])

# Función para centrar la ventana en la pantalla
def centrar_ventana(ventana, ancho=1200, alto=800):
    ventana.update_idletasks()
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    
    x = (pantalla_ancho - ancho) // 2
    y = (pantalla_alto - alto) // 2

    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

# Crear la ventana principal con ttkbootstrap
root = ttk.Window(themename="darkly")  # Tema oscuro moderno
root.title("Conjunto de Mandelbrot y Julia")

# Centrar la ventana
centrar_ventana(root)

# Frame principal para organizar la imagen y los botones
frame = ttk.Frame(root)
frame.pack(pady=10, padx=10)

# Cargar la imagen
ruta_imagen = "mandelbrot.png"  # Cambia esto por la ruta de tu imagen
img = Image.open(ruta_imagen)
img = img.resize((1000, 800))  # Ajustar tamaño
imagen_tk = ImageTk.PhotoImage(img)

# Etiqueta para mostrar la imagen
label_imagen = ttk.Label(frame, image=imagen_tk)
label_imagen.grid(row=0, column=0, rowspan=7, padx=10)

# Lista de archivos .py con estilos de botones
scripts = [
    ("punto1.py", "success"), 
    ("punto2.py", "primary"), 
    ("punto3.py", "danger"), 
    ("punto4A.py", "info"), 
    ("punto4B.py", "warning"), 
    ("punto6.py", "dark"), 
    ("punto7.py", "secondary")
]

# Crear los botones con un "•" en lugar de un icono de carpeta
for i, (script, style) in enumerate(scripts):
    btn = ttk.Button(
        frame, 
        text=f"🔍 {script}",  # Icono de punto "•"
        command=lambda s=script: ejecutar_script(s), 
        bootstyle=style, 
        padding=10
    )
    btn.grid(row=i, column=1, pady=8, padx=15, sticky="w")

# Ejecutar la ventana
root.mainloop()
