from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import numpy as np
import matplotlib.pyplot as plt
import os
from math import sqrt

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Montamos la carpeta "static" para servir archivos estáticos.
app.mount("/static", StaticFiles(directory="static"), name="static")

OUTPUT_FOLDER = "static"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, "fractal.png")

# Función para calcular el fractal (por ejemplo, Mandelbrot)
def calcular_fractal(x_min, x_max, y_min, y_max, ancho, alto, iteraciones_max):
    x = np.linspace(x_min, x_max, ancho)
    y = np.linspace(y_min, y_max, alto)
    c = x + 1j * y[:, None]
    z = np.zeros_like(c, dtype=complex)
    iteraciones = np.zeros(c.shape, dtype=int)
    
    for i in range(iteraciones_max):
        mask = np.abs(z) < 2
        z[mask] = z[mask] ** 2 + c[mask]
        iteraciones[mask] += 1

    # Normalizamos para mejorar la visualización
    iteraciones = np.log(iteraciones + 1) / np.log(iteraciones_max)
    return iteraciones

# Endpoint para generar el fractal a partir de la diagonal ingresada
@app.post("/generar")
async def generar_fractal(diagonal: float = Form(...), iteraciones: int = Form(...)):
    # Para una imagen cuadrada, el lado se obtiene dividiendo la diagonal entre √2.
    side = int(float(diagonal) / sqrt(2))
    ancho = side
    alto = side

    # Definir una región fija del plano complejo para generar el fractal.
    x_min, x_max = -2, 1      # Ancho del plano: 3
    y_min, y_max = -1.5, 1.5    # Alto del plano: 3

    datos_fractal = calcular_fractal(x_min, x_max, y_min, y_max, ancho, alto, iteraciones_max=iteraciones)
    
    # El tamaño de la figura se define en pulgadas: (ancho/dpi, alto/dpi)
    dpi = 100
    plt.figure(figsize=(ancho/dpi, alto/dpi), dpi=dpi)
    plt.imshow(datos_fractal, extent=(x_min, x_max, y_min, y_max), cmap="inferno", origin="lower")
    plt.axis("off")
    plt.savefig(OUTPUT_FILE, bbox_inches="tight", pad_inches=0)
    plt.close()

    return FileResponse(OUTPUT_FILE)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
