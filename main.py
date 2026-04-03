import sys
from operations.basic import add, subtract, multiply, divide
from operations.advanced import power, sqrt, percent

OPERATIONS = {
    '+': (add, 2),
    '-': (subtract, 2),
    '*': (multiply, 2),
    '/': (divide, 2),
    '^': (power, 2),
    'sqrt': (sqrt, 1),
    '%': (percent, 2),
}

def get_number(prompt: str) -> float:
    """."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("error.")

def main():
    print("rtwoin")
    print("operation: +, -, *, /, ^, sqrt, %")
    print("'exit'")
    print("-" * 40)

    while True:
        # Ввод операции
        cmd = input(": ").strip().lower()
        if cmd == 'exit':
            print("idi lesom")
            break

        # Проверка существования операции
        if cmd not in OPERATIONS:
            print(f"inkognito: {cmd}. restart.")
            continue

        func, arity = OPERATIONS[cmd]

        # Сбор аргументов в зависимости от арности
        args = []
        try:
            if arity == 2:
                a = get_number(": ")
                b = get_number(": ")
                args = [a, b]
            elif arity == 1:
                a = get_number(": ")
                args = [a]

            # Вызов функции с распакованными аргументами
            result = func(*args)
            # Форматируем вывод результата в зависимости от операции
            if arity == 2:
                if cmd in ['+', '-', '*', '/', '^']:
                    print(f"{args[0]} {cmd} {args[1]} = {result}")
                elif cmd == '%':
                    print(f"{args[1]}% {args[0]} = {result}")
            else:  # arity == 1
                print(f"{cmd}({args[0]}) = {result}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"error: {e}")

if __name__ == "__main__":
    main()

