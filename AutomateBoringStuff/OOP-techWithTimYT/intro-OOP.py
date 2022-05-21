# OOP in python

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('bark')

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

d = Dog("Tim", 8)
print(d.get_age())
d.set_age(9)
print(d.get_age())

