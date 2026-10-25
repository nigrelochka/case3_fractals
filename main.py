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
    """Настройки черепашки, часть В"""
    pass


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
    """TODO: добавить цикл меню, проверку параметров и вызовы функций."""
    while True:
        show_menu()
        users_choice = input("Выберите пункт меню: ").strip()

        if users_choice == "10":
            print("Завершение программы.")
            break
        elif users_choice == "1":
            depth = get_depth(min_depth=1)
            size = get_size()
            angle = get_angle()
            # Часть В: настройка и рисование дерева
        elif users_choice == "2":
            depth = get_depth()
            size = get_size()
            # Часть В: рисование ветки
        elif users_choice == "3":
            depth = get_depth()
            size = get_size()
            # Часть В: рисование кривой Коха
        elif users_choice == "4":
            depth = get_depth()
            size = get_size()
            # Часть В: рисование снежинки Коха
        elif users_choice == "5":
            depth = get_depth()
            size = get_size()
            # Часть В: рисование кривой Минковского
        elif users_choice == "6":
            depth = get_depth()
            size = get_size()
            # Часть В: рисование ледяного фрактала №1
        elif users_choice == "7":
            depth = get_depth()
            size = get_size()
            # Часть В: рисование ледяного фрактала №2
        elif users_choice == "8":
            depth = get_depth()
            size = get_size()
            # Часть В: рисование кривой Леви
        elif users_choice == "9":
            depth = get_depth()
            size = get_size()
            # Часть В: рисование дракона

        input("Нажмите Enter для возврата в меню...")

if __name__ == "__main__":
    main()
