import random

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from Cuadricula import Punto, Cuadricula
from utils import isPowerOfTwo
app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"])

@app.get("/")
async def root():
    return {"message": "Problema del adoquinamiento, usa los endpoints",
            "endpoints": {
                "/api/{number}/{coord_x_init}/{coord_y_init}": "para especificar donde iniciar",
                "/api/{number}/": "para hacer un definido con un punto inicial aleatorio ",
                "/api": "para hacer todo aleatorio"
            }}


@app.get("/api/{number}/{coord_x_init}/{coord_y_init}")
async def get_point_specified(number: int, coord_x_init: int, coord_y_init: int):

    if not isPowerOfTwo(number):
        raise HTTPException(status_code=400, detail="Must be a power of two")

    if coord_x_init > number or coord_y_init > number:
        raise HTTPException(status_code=400, detail="Baaaad request bae")
    losa_inicial = Punto(coord_x_init, coord_y_init)
    lienzo = Cuadricula(number, losa_inicial)
    lienzo.resolver()
    hola = lienzo.resultado()
    print(hola)

    return {
        "size_canvas": number,
        "init_coords": {
            'x': coord_x_init,
            'y': coord_y_init
        },
        "lista": [lista for lista in hola if len(lista) != 0]
    }


@app.get("/api/{number}")
async def say_hello(number: int):
    if not isPowerOfTwo(number):
        raise HTTPException(status_code=400, detail="Must be a power of two")

    coord_x_init = random.randint(0, number - 1)
    coord_y_init = random.randint(0, number - 1)
    losa_inicial = Punto(coord_x_init, coord_y_init)
    lienzo = Cuadricula(number, losa_inicial)
    lienzo.resolver()
    hola = lienzo.resultado()
    print(hola)

    return {
        "size_canvas": number,
        "init_coords": {
            'x': coord_x_init,
            'y': coord_y_init
        },
        "lista": [lista for lista in hola if len(lista) != 0]
    }


@app.get("/api/")
async def randomize_all():
    number = 2 ** random.randint(2, 5)
    coord_x_init = random.randint(0, number - 1)
    coord_y_init = random.randint(0, number - 1)
    losa_inicial = Punto(coord_x_init, coord_y_init)
    lienzo = Cuadricula(number, losa_inicial)
    lienzo.resolver()
    hola = lienzo.resultado()
    print(hola)

    return {
        "size_canvas": number,
        "init_coords": {
            'x': coord_x_init,
            'y': coord_y_init
        },
        "lista": [lista for lista in hola if len(lista) != 0]
    }