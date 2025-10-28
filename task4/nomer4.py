from __future__ import annotations

class Student:
    def __init__(self, fio: str, age: int, group_number: str, average_grade: float):
        self.fio = fio
        self.age = age
        self.group_number = group_number
        self.average_grade = average_grade

    def show_info(self) -> None:
        print(f"ФИО: {self.fio}, Возраст: {self.age}")

    def scholarship(self) -> int:
        if self.average_grade == 5.0:
            return 6000
        elif self.average_grade < 5.0:
            return 4000
        else:
            return 0

    def compare_scholarship(self, other: 'Student') -> str:
        my_scholarship = self.scholarship()
        other_scholarship = other.scholarship()
        if my_scholarship > other_scholarship:
            return f"Стипендия {self.fio} больше, чем у {other.fio}"
        elif my_scholarship < other_scholarship:
            return f"Стипендия {self.fio} меньше, чем у {other.fio}"
        else:
            return f"Стипендии {self.fio} и {other.fio} равны"


class Postgraduate(Student):
    def __init__(self, fio: str, age: int, group_number: str, average_grade: float, research_title: str):
        super().__init__(fio, age, group_number, average_grade)
        self.research_title = research_title

    def scholarship(self) -> int:
        if self.average_grade == 5.0:
            return 8000
        elif self.average_grade < 5.0:
            return 6000
        else:
            return 0


if __name__ == "__main__":
    stud = Student("Иванов И.И.", 20, "БСБО-01-22", 4.9)
    aspir = Postgraduate("Петрова А.С.", 24, "АСП-01-22", 5.0, "Нейросети в биоинформатике")

    stud.show_info()
    aspir.show_info()

    print("Стипендия студента:", stud.scholarship(), "руб.")
    print("Стипендия аспиранта:", aspir.scholarship(), "руб.")

    print(stud.compare_scholarship(aspir))