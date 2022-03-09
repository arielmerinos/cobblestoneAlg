from Color import Color
from Punto import Punto


class Cuadricula:
    def __init__(self, tamano_cuadricula: int, especial: Punto):
        self.especial = especial
        self.tamano_cuadricula = tamano_cuadricula
        self.array = [[0 for renglon in range(tamano_cuadricula * 2)] for columna in range(tamano_cuadricula * 2)]
        self.array[especial.x][especial.y] = -1
        self.contador = 0

    def asignar_identificador(self, cuadrito1: Punto, cuadrito2: Punto, cuadrito3: Punto ):
        self.contador += 1
        self.array[cuadrito1.x][cuadrito1.y] = self.contador
        self.array[cuadrito2.x][cuadrito2.y] = self.contador
        self.array[cuadrito3.x][cuadrito3.y] = self.contador

    def adoquinar(self, tamano_cuadricula: int, punto: Punto) -> None:
        coordenada_x = punto.x
        coordenada_y = punto.y

        renglon = 0
        columna = 0
        if tamano_cuadricula == 2:
            self.contador += 1
            for numero_columna in range(tamano_cuadricula):
                for numero_renglon in range(tamano_cuadricula):
                    if self.array[coordenada_x + numero_columna][coordenada_y + numero_renglon] == 0:
                        self.array[coordenada_x + numero_columna][coordenada_y + numero_renglon] = self.contador
            return

        for i in range(coordenada_x, coordenada_x + tamano_cuadricula):
            for j in range(coordenada_y, coordenada_y + tamano_cuadricula):
                if self.array[i][j] != 0:
                    renglon = i
                    columna = j

        if renglon < coordenada_x + int(tamano_cuadricula / 2) and columna < coordenada_y + int(tamano_cuadricula / 2):
            cuadrito1 = Punto(coordenada_x + int(tamano_cuadricula / 2), coordenada_y + int(tamano_cuadricula / 2) - 1)
            cuadrito2 = Punto(coordenada_x + int(tamano_cuadricula / 2), coordenada_y + int(tamano_cuadricula / 2))
            cuadrito3 = Punto(coordenada_x + int(tamano_cuadricula / 2) - 1, coordenada_y + int(tamano_cuadricula / 2))
            self.asignar_identificador( cuadrito1, cuadrito2, cuadrito3)

        elif renglon >= coordenada_x + int(tamano_cuadricula / 2) and columna < coordenada_y + int(tamano_cuadricula / 2):
            cuadrito1 = Punto(coordenada_x + int(tamano_cuadricula / 2) - 1, coordenada_y + int(tamano_cuadricula / 2))
            cuadrito2 = Punto(coordenada_x + int(tamano_cuadricula / 2), coordenada_y + int(tamano_cuadricula / 2))
            cuadrito3 = Punto(coordenada_x + int(tamano_cuadricula / 2) - 1, coordenada_y + int(tamano_cuadricula / 2) - 1)
            self.asignar_identificador(cuadrito1, cuadrito2, cuadrito3)

        elif renglon < coordenada_x + int(tamano_cuadricula / 2) and columna >= coordenada_y + int(tamano_cuadricula / 2):
            cuadrito1 = Punto(coordenada_x + int(tamano_cuadricula / 2), coordenada_y + int(tamano_cuadricula / 2) - 1)
            cuadrito2 = Punto(coordenada_x + int(tamano_cuadricula / 2), coordenada_y + int(tamano_cuadricula / 2))
            cuadrito3 = Punto(coordenada_x + int(tamano_cuadricula / 2) - 1, coordenada_y + int(tamano_cuadricula / 2) - 1)
            self.asignar_identificador(cuadrito1, cuadrito2, cuadrito3)

        elif renglon >= coordenada_x + int(tamano_cuadricula / 2) and columna >= coordenada_y + int(tamano_cuadricula / 2):
            cuadrito1 = Punto(coordenada_x + int(tamano_cuadricula / 2) - 1, coordenada_y + int(tamano_cuadricula / 2))
            cuadrito2 = Punto(coordenada_x + int(tamano_cuadricula / 2), coordenada_y + int(tamano_cuadricula / 2) - 1)
            cuadrito3 = Punto(coordenada_x + int(tamano_cuadricula / 2) - 1, coordenada_y + int(tamano_cuadricula / 2) - 1)
            self.asignar_identificador(cuadrito1, cuadrito2, cuadrito3)

        cuadrante1 = Punto(coordenada_x, coordenada_y + int(tamano_cuadricula / 2))
        self.adoquinar(int(tamano_cuadricula / 2), cuadrante1)

        cuadrante2 = Punto(coordenada_x, coordenada_y)
        self.adoquinar(int(tamano_cuadricula / 2), cuadrante2)

        cuadrante3 = Punto(coordenada_x + int(tamano_cuadricula / 2), coordenada_y)
        self.adoquinar(int(tamano_cuadricula / 2), cuadrante3)

        cuadrante4 = Punto( coordenada_x + int(tamano_cuadricula / 2), coordenada_y + int(tamano_cuadricula / 2))
        self.adoquinar(int(tamano_cuadricula / 2), cuadrante4)

    def resolver(self):
        self.adoquinar(self.tamano_cuadricula, Punto(0, 0))

    def resultado(self):
        color = Color()
        return [[color.colorear(numero) for numero in renglon if numero != 0] for renglon in self.array]
