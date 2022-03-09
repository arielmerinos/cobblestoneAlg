import random

from fastapi import FastAPI
from Cuadricula import Punto, Cuadricula
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Problema del adoquinamiento"}


@app.get("/api/{number}")
async def say_hello(number: int):
    coord_x_init = random.randint(0, number - 1)
    coord_y_init = random.randint(0, number - 1)
    losa_inicial = Punto(coord_x_init, coord_y_init)
    lienzo = Cuadricula(number, losa_inicial)
    lienzo.resolver()
    hola = lienzo.resultado()
    print(hola)

    return {
        "init_coords": {
            'x': coord_x_init,
            'y': coord_y_init
        },
        "lista": [lista for lista in hola if len(lista) != 0]
    }
