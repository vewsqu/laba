class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        """
        Конструктор базового класса Vehicle.

        :param make: Производитель транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self.make = make
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """Возвращает строковое представление объекта."""
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self) -> str:
        """Возвращает непривилегированное представление объекта."""
        return f"Vehicle(make='{self.make}', model='{self.model}', year={self.year})"

    def start_engine(self) -> str:
        """Запускает двигатель транспортного средства."""
        return f"The engine of {self.make} {self.model} is now running."


class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, doors: int):
        """
        Конструктор класса Car, наследует от Vehicle и добавляет атрибут doors.

        :param doors: Количество дверей в автомобиле.
        """
        super().__init__(make, model, year)
        self.__doors = doors  # Инкапсуляция, количество дверей не должно быть доступно напрямую

    def __str__(self) -> str:
        """Возвращает строковое представление объекта, расширенное для автомобиля."""
        return super().__str__() + f", Doors: {self.__doors}"

    def __repr__(self) -> str:
        """Возвращает непривилегированное представление объекта, расширенное для автомобиля."""
        return f"Car(make='{self.make}', model='{self.model}', year={self.year}, doors={self.__doors})"

    def start_engine(self) -> str:
        """Переопределяет метод для предоставления информации о запуске двигателя автомобиля.

        Эта версия также сообщает количество дверей, что может быть полезно для водителя.
        """
        base_message = super().start_engine()
        return f"{base_message} This car has {self.__doors} doors."


my_car = Car("Toyota", "Camry", 2021, 4)
print(my_car)
print(repr(my_car))
print(my_car.start_engine())

