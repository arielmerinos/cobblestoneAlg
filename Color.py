import random


class Color:
    def __init__(self):
        self.color_values = [
            "#F6E7D8",
            '#7976e8',
            '#6764c6',
            '#8784ff',
            '#5899fb',
            '#0E3EDA',
            '#3a5aff',
            '#0c36be',
            '#0b2ea2',
            '#09278b',
            '#641f8b',
            '#8e00ce',
            '#8400bd',
            '#c15e90',
            '#b53086',
            '#ff45bc',
            '#e26aab',
            '#F473B9',
            '#ffaad4',
            '#FFBDE6',
            '#FFDDEE',
        ]

    def colorear(self, identificador: int):
        color = {
            'id': identificador,
            'color': self.color_values[identificador % len(self.color_values)]
        }
        return color
