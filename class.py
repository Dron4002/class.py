class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def bark(self):
        print(f"Dog named {self.name} is barking")
class Cat(Animal):
    def __init__(self, name):
        self.name = name
    def meow(self):
        print(f"{self.name} says meow")
class Frog(Animal):
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"Frog with name {self.name} is eating")


d = Dog("Sharik", "Newfoundland")
c = Cat("Murka")
f = Frog("Kwa")
d.bark()
d.breed
d.eat()
c.eat()
f.eat()
c.meow()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Junior_programmer(Person):
    def __init__(self, name, age, duties):
        super().__init__(name, age)
        self.duties = duties
    def exercises(self):
        print(f"{self.name} с возрастом {self.age} {self.duties}")
class Senior_programmer(Person):
    def __init__(self, name, age, duties):
        super().__init__(name, age)
        self.duties = duties
    def exercises(self):
        print(f"{self.name} с возрастом {self.age} {self.duties}")
j = Junior_programmer("Андрей", "22 года", "решает самые простые задачи")
s = Senior_programmer("Александр", "43 года", "создает сайты, игры, мобильные приложения и решает самые сложные задачи")
s.exercises()
j.exercises()

