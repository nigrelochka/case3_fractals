"""Роль 3: сложные фракталы."""
from math import sqrt
from turtle import *


def ice_fractal_1(order: int, size: float) -> None:
    """TODO: ледяной фрактал №1."""
    if order == 0:
        fd(size)
        return
    ice_fractal_1(order - 1, size / 2)
    lt(90)
    ice_fractal_1(order - 1, size / 4)
    rt(180)
    ice_fractal_1(order - 1, size / 4)
    lt(90)
    ice_fractal_1(order - 1, size / 2)

speed(0)
pu()
goto(-200, 0)
pd()
#ice_fractal_1(2, 300)

# hideturtle()



def ice_fractal_2(order: int, size: float) -> None:
    """TODO: ледяной фрактал №2."""
    if order == 0:
        fd(size)
        return
    ice_fractal_2(order - 1, size)
    lt(120)
    ice_fractal_2(order - 1, size / 2)
    rt(180)
    ice_fractal_2(order - 1, size / 2)
    lt(120)
    ice_fractal_2(order - 1, size / 2)
    rt(180)
    ice_fractal_2(order - 1, size / 2)
    lt(120)
    ice_fractal_2(order - 1, size)

speed(0)
pu()
goto(-200, 0)
pd()
#ice_fractal_2(2, 100)

# hideturtle()


def levy(order: int, size: float) -> None:
    """TODO: кривая Леви."""
    if order == 0:
        fd(size)
        return
    lt(45)
    levy(order - 1, size / sqrt(2))
    rt(90)
    levy(order - 1, size / sqrt(2))
    lt(45)

speed(0)
pu()
goto(-200, 0)
pd()
#levy(10, 300)

# hideturtle()


def dragon(order: int, size: float, turn: int = 1) -> None:
    """TODO: дракон Хартера-Хейтуэя."""

    if order == 0:
        fd(size)
        return
    lt(45)
    dragon(order - 1, size / sqrt(2), 1)
    rt(90 * turn)
    dragon(order - 1, size / sqrt(2), -1)
    rt(45)

speed(0)
pu()
goto(-200, 0)
pd()
#dragon(2, 300)

# hideturtle()

done()