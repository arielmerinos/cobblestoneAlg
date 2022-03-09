

class Punto:
    def __init__(self, coordenada_x: int, coordenada_y: int) -> None:
        self._x = coordenada_x
        self._y = coordenada_y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y