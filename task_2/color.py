from enum import Enum, auto


class Color(Enum):
    RED = auto()
    BLACK = auto()
    EMPTY = auto()


def get_opposite_color(color):
    if color is Color.RED:
        return Color.BLACK
    elif color is Color.BLACK:
        return Color.RED
    else:
        raise Exception
