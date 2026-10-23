"""Роль 4: меню и интеграция."""
from fractals.basic import draw_binary_tree, draw_branch
from fractals.koch import koch, koch_snowflake, minkowski
from fractals.complex import ice_fractal_1, ice_fractal_2, levy, dragon

def show_menu() -> None:
    print("=== ФРАКТАЛЬНАЯ МАСТЕРСКАЯ ===")
    print("1. Двоичное дерево\n2. Ветка\n3. Кривая Коха")
    print("4. Снежинка Коха\n5. Кривая Минковского")
    print("6. Ледяной фрактал №1\n7. Ледяной фрактал №2")
    print("8. Кривая Леви\n9. Дракон Хартера-Хейтуэя\n10. Выход")

def main() -> None:
    """TODO: добавить цикл меню, проверку параметров и вызовы функций."""
    show_menu()

if __name__ == "__main__":
    main()
