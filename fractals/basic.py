import turtle


def draw_binary_tree(depth: int, size: float, angle: float) -> None:
    """Рисует двоичное дерево с помощью рекурсии."""
    if depth == 0:
        turtle.backward(size)
        return

        turtle.forward(size)

        turtle.right(angle)
        draw_binary_tree(depth - 1, size / 2, angle)

        turtle.left(angle)
        turtle.left(angle)
        draw_binary_tree(depth - 1, size / 2, angle)

        turtle.right(angle)
        turtle.backward(size)


def draw_branch(n: int, size: float) -> None:
    """Рисует ветку с помощью рекурсии."""
    if n == 0:
        turtle.backward(size)
        return

    turtle.forward(size)

    turtle.left(60)
    draw_branch(n - 1, size / 2.5)
    turtle.right(60)

    turtle.right(60)
    draw_branch(n - 1, size / 2.5)
    turtle.left(60)

    draw_branch(n - 1, size)

    turtle.backward(size)
