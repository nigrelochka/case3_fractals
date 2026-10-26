import turtle


def draw_binary_tree(depth: int, size: float, angle: float) -> None:
    """Рисует двоичное дерево с помощью рекурсии."""
    if depth == 0:
        turtle.forward(size)
        turtle.backward(size)
    else:
        turtle.forward(size)

        turtle.right(angle)
        draw_binary_tree(depth - 1, size / 2, angle)

        turtle.left(angle)
        turtle.left(angle)
        draw_binary_tree(depth - 1, size / 2, angle)

        turtle.right(angle)
        turtle.backward(size)


def draw_branch(n: int, size: float) -> None:
    """Рисует фрактал «Ветка» с помощью рекурсии."""
    if n == 0:
        turtle.forward(size)
        turtle.backward(size)
    else:
        turtle.forward(size)

        turtle.left(30)
        draw_branch(n - 1, size / 2)

        turtle.right(60)
        draw_branch(n - 1, size / 2)

        turtle.left(30)
        turtle.backward(size)
