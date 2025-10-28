from typing import Callable, Iterable, List

def filter_strings(
    filter_func: Callable[[str], bool],
    strings: Iterable[str]
) -> List[str]:
    return list(filter(filter_func, strings))


# Тестовые данные
test_strings = [
    "apple",
    "banana",
    "aardvark",
    "hello world",
    "test",
    "alpha",
    "gamma",
    "a",
    "python",
    "code"
]

# Примеры использования
no_spaces = filter_strings(lambda s: ' ' not in s, test_strings)
not_start_with_a = filter_strings(lambda s: not s.startswith('a'), test_strings)
length_at_least_5 = filter_strings(lambda s: len(s) >= 5, test_strings)

print("Без пробелов:", no_spaces)
print("Не начинаются с 'a':", not_start_with_a)
print("Длина >= 5:", length_at_least_5)