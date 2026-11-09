from inventory import show_equipment


def main():
    while True:
        print("\n=== Система учёта инвентаря ===")
        print("1. Показать оборудование")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            show_equipment()
        elif choice == '0':
            print("Выход из программы...")
            break
        else:
            print("Ошибка: Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()