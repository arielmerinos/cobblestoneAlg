import random


class Color:
    def __init__(self):
        self.color_values = [
            "#F6E7D8",
            '#F68989',
            '#C65D7B',
            '#874356',
            '#0E3EDA',
            '#F473B9',
            '#FFBDE6',
            '#FFDDEE',
            '#E2DEA9',
        ]

    def colorear(self, identificador: int):
        color = {
            'id': identificador,
            'color': self.color_values[identificador % len(self.color_values)]
        }
        return color
