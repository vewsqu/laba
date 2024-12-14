import doctest


class Furniture:
    def __init__(self, material: str, weight: float, height: float):
        self.material = material
        self.weight = weight
        self.height = height
        self.validate()

    def validate(self):
        if self.weight <= 0:
            raise ValueError("Вес мебели должен быть положительным числом.")
        if self.height <= 0:
            raise ValueError("Высота мебели должна быть положительным числом.")

    def assemble(self) -> None:
        print(f"Собираем мебель из {self.material}.")

    def disassemble(self) -> None:
        print("Разбираем мебель.")


class Vehicle:
    def __init__(self, wheels: int, color: str):
        self.wheels = wheels
        self.color = color
        self.validate()

    def validate(self):
        if self.wheels <= 0:
            raise ValueError("Количество колес должно быть положительным числом.")

    def drive(self, distance: float) -> None:
        print(f"Едем на {distance} км.")

    def stop(self) -> None:
        print("Останавливаемся.")


class DigitalService:
    def __init__(self, name: str, users: int):
        self.name = name
        self.users = users
        self.validate()

    def validate(self):
        if self.users < 0:
            raise ValueError("Количество пользователей не может быть отрицательным числом.")

    def add_user(self) -> None:
        self.users += 1
        print(f"Добавлен пользователь. Теперь пользователей: {self.users}.")

    def remove_user(self) -> None:
        if self.users > 0:
            self.users -= 1
            print(f"Удален пользователь. Теперь пользователей: {self.users}.")
        else:
            print("Нет пользователей для удаления.")


if __name__ == "__main__":
    doctest.testmod()
    pass
