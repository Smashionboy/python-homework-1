from abc import ABC, abstractmethod
import math

class Figure(ABC):

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def area_comparer(self, other: 'Figure') -> bool:
        return self.area() > other.area()


    def perimeter_comparer(self, other: 'Figure') -> bool:
        return self.perimeter() > other.perimeter()




class Square(Figure):
    def __init__(self, side: float):
        if side <= 0:
            raise ValueError("Сторона квадрата должна быть положительной")
        self.side = side

    def area(self) -> float:
        return self.side ** 2

    def perimeter(self) -> float:
        return 4 * self.side


class Rectangle(Figure):
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Стороны треугольника должны быть положительными")

        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Невозможно построить треугольник с такими сторонами")
        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self) -> float:
        return self.a + self.b + self.c


class Circle(Figure):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Радиус круга должен быть положительным")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


# Пример использования
if __name__ == "__main__":
    square = Square(4)
    rect = Rectangle(3, 5)
    triangle = Triangle(3, 4, 5)
    circle = Circle(3)

    print("Площади:")
    print(f"Квадрат: {square.area():.2f}")
    print(f"Прямоугольник: {rect.area():.2f}")
    print(f"Треугольник: {triangle.area():.2f}")
    print(f"Круг: {circle.area():.2f}")

    print("\nСравнение площадей:")
    print(f"Площадь круга > площади квадрата? {circle.area_comparer(square)}")
    print(f"Площадь треугольника < площади прямоугольника? {triangle.area_comparer(rect)}")

    print("\nСравнение периметров:")
    print(f"Периметр квадрата > периметра треугольника? {square.perimeter_comparer(triangle)}")
    print(f"Периметр круга < периметра прямоугольника? {circle.perimeter_comparer(rect)}")