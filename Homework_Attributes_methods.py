"""
Пункты задачи:
Создайте класс House.
Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
Создайте объект класса House с произвольным названием и количеством этажей.
Вызовите метод go_to у этого объекта с произвольным числом.
"""

class House:
    def __init__(self, name, number_of_floors):
        # Инициализация атрибутов
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # Проверка, существует ли такой этаж
        if 1 <= new_floor <= self.number_of_floors:
            # Вывод всех этажей от 1 до нового этажа
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

# Пример использования:
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# Вызовы метода go_to
h1.go_to(5)
h2.go_to(10)