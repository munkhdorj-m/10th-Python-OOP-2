# ---------------------------------------------------
# Exercise 1 — Shape → Rectangle
# ---------------------------------------------------

class Shape:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)  # inherit name
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# ---------------------------------------------------
# Exercise 2 — Animal → Dog
# ---------------------------------------------------

class Animal:
    def sound(self):
        return "Some sound"


class Dog(Animal):
    def sound(self):
        return "Bark"


# ---------------------------------------------------
# Exercise 3 — Employee → Manager
# ---------------------------------------------------

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def total_salary(self):
        return self.salary + self.bonus
