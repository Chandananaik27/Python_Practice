class Person:
    def __init__(self, name):
        self.__name = name  # private variable

    def get_name(self):
        return self.__name  # public method to access private data

    def set_name(self, name):
        self.__name = name  # public method to modify private data

# Using the class
p = Person("Chandana")
print(p.get_name())  # Accessing private data safely
p.set_name("Chandra")
print(p.get_name())

#delete Keyword
class student:
    def __init__(self,name):
        self.name=name
s1=student("chandana")
del s1
print(s1.name)
