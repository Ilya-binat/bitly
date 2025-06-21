class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Гав-гав!")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Счет пополнен на {amount}. Текущий баланс: {self.balance}")
        else:
            print("Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств для снятия.")
        elif amount <= 0:
            print("Сумма снятия должна быть положительной.")
        else:
            self.balance -= amount
            print(f"Снято {amount}. Текущий баланс: {self.balance}")


class Animal:
    def eat(self):
        print("Животное ест.")

    def sleep(self):
        print("Животное спит.")

class Cat(Animal):
    def meow(self):
        print("Мяу!")


class Shape:

    def are(self):
        return 0
class Circle(Shape):
    def area(self, radius):
        return 3,14 * radius **2
class Square(Shape):
    def area(self, side):
        return side **2