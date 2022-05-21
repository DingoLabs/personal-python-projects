# OOP practice file

class Hippo:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def moo(self):
        print("moo")

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(self.age)

    def birthday(self):
        self.age += 1

    def set_name(self, name):
        self.name = name

h = Hippo("hilary", 5)
h.moo()
h.get_name()
h.get_age()
h.birthday()
h.get_age()
h.set_name("tipper")
h.get_name()
h.__init__("barbara",5)
h.get_name()