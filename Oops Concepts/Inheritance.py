class car:
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")
class ToyotaCar(car):
    def __init__(self,name):
        self.name=name
car1=ToyotaCar("fortuner")
car2=ToyotaCar("maruti")
print(car1.name)
print(car1.start())

#single inheritance
class Parent:
    def show(self):
        print("This is the Parent class")

class Child(Parent):
    def display(self):
        print("This is the Child class")

obj = Child()
obj.show()     # Inherited from Parent
obj.display()

#multilevel inheritance
class Grandparent:
    def house(self):
        print("Grandparent's house")

class Parent(Grandparent):
    def car(self):
        print("Parent's car")

class Child(Parent):
    def bike(self):
        print("Child's bike")

c = Child()
c.house()
c.car()
c.bike()

#multiple inheritance
class Mother:
    def cook(self):
        print("Mother can cook")

class Father:
    def drive(self):
        print("Father can drive")

class Child(Mother, Father):
    def play(self):
        print("Child can play")

c = Child()
c.cook()
c.drive()
c.play()



