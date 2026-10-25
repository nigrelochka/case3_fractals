"""Роль 2: Кох и Минковский."""

import turtle


def koch(order: int, size: float) -> None:
    """Рисует кривую Коха."""
    if order == 0:
        turtle.forward(size)
        return

    koch(order - 1, size / 3)
    turtle.left(60)
    koch(order - 1, size / 3)
    turtle.right(120)
    koch(order - 1, size / 3)
    turtle.left(60)
    koch(order - 1, size / 3)


def koch_snowflake(order: int, size: float) -> None:
    """Рисует снежинку Коха."""
    for _ in range(3):
        koch(order, size)
        turtle.right(120)


def minkowski(order: int, size: float) -> None:
    """Рисует кривую Минковского."""
    if order == 0:
        turtle.forward(size)
        return

    segment = size / 4
    turns = [0, 90, -90, -90, 90, 90, -90, 0]

    for angle in turns:
        turtle.left(angle)
        minkowski(order - 1, segment)