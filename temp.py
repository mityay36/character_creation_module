from math import sqrt

message = """Добро пожаловать в самую лучшую программу
 для вычисления квадратного корня из заданного числа"""


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> float:
    """Произодит вычисление корня из введенного числа."""
    result: float = calculate_square_root(your_number)
    print("Мы вычислили квадратный корень из введённого вами числа."
          f" Это будет: {result}")
    return result


print(message)
calc(25.5)
