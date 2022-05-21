


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_drinking_age(self):
        my_age = self.age
        my_name = self.name
        if not my_age >= 21:
            years_to_go = 21 - my_age
            return "you have " + str(years_to_go) + " years to go, " + my_name + "!"
        return "go get hammered " + my_name + "!"

p1 = Person("Phil", 35)
p2 = Person("Not-Phil", 4)
print(p1.is_drinking_age())
print(p2.is_drinking_age())
