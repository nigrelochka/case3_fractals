"""Роль 4: меню и интеграция."""
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

def main() -> None:
    """TODO: добавить цикл меню, проверку параметров и вызовы функций."""
    while True:
        show_menu()
        users_choice = input("Выберите пункт меню: ").strip()

        if users_choice == "10":
            print("Завершение программы.")
            break
        elif users_choice == "1":
            pass  # Часть Б и В
        elif users_choice == "2":
            pass  # Часть Б и В
        elif users_choice == "3":
            pass  # Часть Б и В
        elif users_choice == "4":
            pass  # Часть Б и В
        elif users_choice == "5":
            pass  # Часть Б и В
        elif users_choice == "6":
            pass  # Часть Б и В
        elif users_choice == "7":
            pass  # Часть Б и В
        elif users_choice == "8":
            pass  # Часть Б и В
        elif users_choice == "9":
            pass  # Часть Б и В

        input("Нажмите Enter для возврата в меню...")

if __name__ == "__main__":
    main()
