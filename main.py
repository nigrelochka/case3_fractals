"""Роль 4: меню и интеграция."""

import math
import turtle

from fractals.basic import draw_binary_tree, draw_branch
from fractals.koch import koch, koch_snowflake, minkowski
from fractals.complex import ice_fractal_1, ice_fractal_2, levy, dragon


def show_menu() -> None:
    print("=== ФРАКТАЛЬНАЯ МАСТЕРСКАЯ ===")
    print("1. Двоичное дерево\n2. Ветка\n3. Кривая Коха")
    print("4. Снежинка Коха\n5. Кривая Минковского")
    print("6. Ледяной фрактал №1\n7. Ледяной фрактал №2")
    print("8. Кривая Леви\n9. Дракон Хартера-Хейтуэя\n10. Выход")

def setup_turtle():
    """Настраивает окно и черепашку перед рисованием."""
    turtle.reset()
    turtle.title('Фрактальная мастерская')
    turtle.setup(1000, 750)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.tracer(1,0)
    turtle.penup()
    turtle.goto(0, -150)
    turtle.pendown()


# Ввод и проверка параметров.
def get_depth(min_depth: int = 0,
              max_depth: int | None = None) -> int:
    """Запрашивает допустимую глубину рекурсии."""
    while True:
        try:
            depth = int(input("Глубина рекурсии: "))

            if depth < min_depth:
                print(f"Глубина должна быть не меньше {min_depth}.")
                continue

            if max_depth is not None and depth > max_depth:
                print(f"Глубина должна быть не больше {max_depth}.")
                continue

            return depth

        except ValueError:
            print("Ошибка: необходимо ввести целое число.")


def get_size() -> float:
    """Запрашивает положительный размер фрактала."""
    while True:
        try:
            size = float(input("Размер фрактала: "))

            if math.isfinite(size) and size > 0:
                return size

            print("Размер должен быть положительным числом.")

        except ValueError:
            print("Ошибка: необходимо ввести число.")


def get_angle() -> float:
    """Запрашивает угол от 0 до 90 градусов."""
    while True:
        try:
            angle = float(input("Угол от 0 до 90 градусов: "))

            if math.isfinite(angle) and 0 <= angle <= 90:
                return angle

            print("Угол должен быть от 0 до 90 градусов.")

        except ValueError:
            print("Ошибка: необходимо ввести число.")


def main() -> None:
    """Запускает меню и рисует выбранный фрактал."""
    while True:
        show_menu()
        users_choice = input('Выберите пункт меню: ').strip()

        if users_choice == '10':
            print('Завершение программы.')
            break

        elif users_choice == '1':
            depth = get_depth(min_depth=1, max_depth=9)
            size = get_size()
            angle = get_angle()

            setup_turtle()
            turtle.left(90)
            draw_binary_tree(depth, size, angle)

        elif users_choice == '2':
            depth = get_depth(max_depth=9)
            size = get_size()

            setup_turtle()
            turtle.left(90)
            draw_branch(depth, size)

        elif users_choice == '3':
            depth = get_depth(max_depth=6)
            size = get_size()

            setup_turtle()
            turtle.penup()
            turtle.goto(-300, 0)
            turtle.pendown()
            koch(depth, size)

        elif users_choice == '4':
            depth = get_depth(max_depth=6)
            size = get_size()

            setup_turtle()
            turtle.penup()
            turtle.goto(-size / 2, 150)
            turtle.pendown()
            koch_snowflake(depth, size)

        elif users_choice == '5':
            depth = get_depth(max_depth=4)
            size = get_size()

            setup_turtle()
            turtle.penup()
            turtle.goto(-300, 0)
            turtle.pendown()
            minkowski(depth, size)

        elif users_choice == '6':
            depth = get_depth(max_depth=6)
            size = get_size()

            setup_turtle()
            turtle.penup()
            turtle.goto(-300, 0)
            turtle.pendown()
            ice_fractal_1(depth, size)

        elif users_choice == '7':
            depth = get_depth(max_depth=4)
            size = get_size()

            setup_turtle()
            turtle.penup()
            turtle.goto(-300, 0)
            turtle.pendown()
            ice_fractal_2(depth, size)

        elif users_choice == '8':
            depth = get_depth(max_depth=12)
            size = get_size()

            setup_turtle()
            turtle.penup()
            turtle.goto(-size / 2, 0)
            turtle.pendown()
            levy(depth, size)

        elif users_choice == '9':
            depth = get_depth(max_depth=12)
            size = get_size()

            setup_turtle()
            turtle.penup()
            turtle.goto(-size / 2, 0)
            turtle.pendown()
            dragon(depth, size)

        else:
            print('Такого пункта нет.')
            continue

        turtle.update()
        input('Нажмите Enter для возврата в меню...')

    turtle.bye()

if __name__ == "__main__":
    main()
