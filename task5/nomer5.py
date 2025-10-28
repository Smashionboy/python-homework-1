import time
from functools import wraps
import logging

logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
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
        logging.error(f"Ошибка: файл {input_path} не найден. Убедитесь, что он существует в папке с программой.")
        raise
    except ValueError as e:
        logging.exception(f"Ошибка при чтении чисел: {e}")
        raise

if __name__ == "__main__":
    add_numbers_console(100, 200)
    print("-" * 40)
    add_numbers_from_file()