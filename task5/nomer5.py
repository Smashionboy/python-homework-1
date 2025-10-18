import time
from functools import wraps


def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Функция '{func.__name__}' выполнена за {end_time - start_time:.6f} секунд")
        return result
    return wrapper

@timing_decorator
def add_numbers_console(a: float, b: float) -> float:
    result = a + b
    print(f"Сумма {a} + {b} = {result}")
    return result

@timing_decorator
def add_numbers_from_file(input_path: str = "input.txt", output_path: str = "output.txt") -> float:
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = f.read().strip().split()
            if len(data) < 2:
                raise ValueError("Файл должен содержать минимум два числа")
            a = float(data[0])
            b = float(data[1])

        result = a + b

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"{result}\n")

        print(f"Результат записан в {output_path}: {result}")
        return result

    except FileNotFoundError:
        print(f"Ошибка: файл {input_path} не найден. Убедитесь, что он существует в папке с программой.")
        raise
    except ValueError as e:
        print(f"Ошибка при чтении чисел: {e}")
        raise

if __name__ == "__main__":
    add_numbers_console(100, 200)
    print("-" * 40)
    add_numbers_from_file()