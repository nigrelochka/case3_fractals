"""Роль 3: сложные фракталы."""
from math import sqrt
import turtle


def ice_fractal_1(order: int, size: float) -> None:
    """TODO: ледяной фрактал №1."""
    if order == 0:
        turtle.fd(size)
        return
    ice_fractal_1(order - 1, size / 2)
    turtle.lt(90)
    ice_fractal_1(order - 1, size / 4)
    turtle.rt(180)
    ice_fractal_1(order - 1, size / 4)
    turtle.lt(90)
    ice_fractal_1(order - 1, size / 2)


def ice_fractal_2(order: int, size: float) -> None:
    """TODO: ледяной фрактал №2."""
    if order == 0:
        turtle.fd(size)
        return
    ice_fractal_2(order - 1, size)
    turtle.lt(120)
    ice_fractal_2(order - 1, size / 2)
    turtle.rt(180)
    ice_fractal_2(order - 1, size / 2)
    turtle.lt(120)
    ice_fractal_2(order - 1, size / 2)
    turtle.rt(180)
    ice_fractal_2(order - 1, size / 2)
    turtle.lt(120)
    ice_fractal_2(order - 1, size)


def levy(order: int, size: float) -> None:
    """TODO: кривая Леви."""
    if order == 0:
        turtle.fd(size)
        return
    turtle.lt(45)
    levy(order - 1, size / sqrt(2))
    turtle.rt(90)
    levy(order - 1, size / sqrt(2))
    turtle.lt(45)


def dragon(order: int, size: float, turn: int = 1) -> None:
    """TODO: дракон Хартера-Хейтуэя."""

    if order == 0:
        turtle.fd(size)
        return
    turtle.lt(45)
    dragon(order - 1, size / sqrt(2), 1)
    turtle.rt(90 * turn)
    dragon(order - 1, size / sqrt(2), -1)
    turtle.rt(45)
