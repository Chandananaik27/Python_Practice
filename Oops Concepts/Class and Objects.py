class student:
    name="chandu"
s1=student()
print(s1.name)
s2=student()
print(s2.name)

class car:
    color="blue"
    brand="bmw"
car1=car()
print(car1.color)
print(car1.brand)

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s1=student("chandana",98)
print(s1.name,s1.marks)
s2=student("chai",90)
print(s2.name,s2.marks)

class student:
    name="chandana"
    college="oxford" #class attribute
    def __init__(self,age):
        self.age=age #object attribute
s1=student(45)
print(s1.name,s1.college)



