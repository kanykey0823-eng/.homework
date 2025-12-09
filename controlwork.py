class Animal:
    def __init__(self, name, age):
        self.__name = name   # приватный атрибут
        self.__age = age     # приватный атрибут

    # --- name ---
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    # --- age ---
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print("Возраст не может быть отрицательным!")

    def make_sound(self):
        return "Какой-то звук животного"


class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"


class Cat(Animal):
    def make_sound(self):
        return "Мяу-Мяу!"


# --- Проверка работы ---
if __name__ == "__main__":
    dog = Dog("Шарик", 3)
    cat = Cat("Мурка", 2)

    print(dog.name, "-", dog.make_sound())
    print(cat.name, "-", cat.make_sound())

    # Меняем значения приватных атрибутов через сеттеры
    dog.name = "Бобик"
    dog.age = 5

    cat.name = "Снежок"
    cat.age = 4

    print(dog.name, dog.age)
    print(cat.name, cat.age)
