import random


class Color:
    def __init__(self):
        self.color_values = [
            "#F6E7D8",
            '#ffd358',
            '#fb913e',
            '#8784ff',
            '#b2192b',
            '#00edff',
            '#ff5a82',
            '#640134',
            '#0b2ea2',
            '#89f070',
            '#641f8b',
            '#00673c',
            '#9fd83b',
            '#4c6e3c',
            '#b53086',
            '#ff45bc',
            '#3c2a40',
            '#2a3c3e',
            '#ffaad4',
            '#74d8bc',
            '#FFDDEE',
        ]

    def colorear(self, identificador: int):
        color = {
            'id': identificador,
            'color': self.color_values[identificador % len(self.color_values)]
        }
        return color
