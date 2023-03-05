import math
import random


def test_greeting():
    name = "Анна"
    age = 25
    output = f"Привет, {name}! Тебе {age} лет."
    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    a = 10
    b = 20
    perimeter = (a + b) * 2
    assert perimeter == 60
    print(perimeter)
    area = a * b
    assert area == 200


def test_circle():
    r = 23
    area = math.pi * math.pow(r, 2)
    assert area == 1661.9025137490005
    length = 2 * math.pi * r
    assert length == 144.51326206513048


def test_random_list():
    l = sorted([random.randint(0, 100) for l in range(10)])
    assert len(l) == 10
    assert l[0] < l[-1]
    print(l)


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # Преобразование списка во множество
    l = list(set(l))
    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(l)


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Выведите на экран все значения словаря.
    Подсказка: используй встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    d = dict(zip(first, second))
    print(d)
    assert isinstance(d, dict)
    assert len(d) == 5
