def calculator():
    print("=== Простой калькулятор ===")
    print("Доступные операции: +, -, *, /")
    print("Для выхода введите 'q' в поле оператора.\n")

    while True:
        # Ввод первого числа
        first_input = input("Введите первое число (или 'q' для выхода): ").strip()
        if first_input.lower() == 'q':
            print("Выход из калькулятора. До свидания!")
            break

        # Валидация первого числа
        try:
            num1 = float(first_input)
        except ValueError:
            print("Ошибка: это не число. Попробуйте снова.\n")
            continue

        # Ввод оператора
        op = input("Введите операцию (+, -, *, /): ").strip()
        if op.lower() == 'q':
            print("Выход из калькулятора. До свидания!")
            break

        # Валидация оператора
        if op not in ('+', '-', '*', '/'):
            print("Ошибка: недопустимая операция. Доступны только +, -, *, /.\n")
            continue

        # Ввод второго числа
        second_input = input("Введите второе число: ").strip()
        try:
            num2 = float(second_input)
        except ValueError:
            print("Ошибка: это не число. Попробуйте снова.\n")
            continue

        # Выполнение операции
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Ошибка: деление на ноль невозможно.\n")
                continue
            result = num1 / num2

        # Красивый вывод результата
        # Если число целое — показываем без .0
        if result == int(result):
            result = int(result)

        print(f"Результат: {num1} {op} {num2} = {result}\n")


if name == "main":
    calculator()
