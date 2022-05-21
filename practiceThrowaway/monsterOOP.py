
class Monster:
    # def __init__(self, health):
    #     self.health = health
    health = 20

    def move(self, move):
        print("monster moves " + str(move) + " spaces")

    def get_damage(self, amount):
        print("monster receieves " + str(amount) + " of damage")
        self.health -= amount
        print ("health left: " + str(self.health))

class Shark(Monster):
    def __init__(self, speed):
        self.speed = speed

    def bite(self):
        print('the shark has bitten')

class Hero():
    def __init__(self,damage, monster):
        self.damage = damage
        self.monster = monster

    def give_damage(self):
        self.monster.get_damage(self.damage)
        


m = Monster()
h = Hero(15, m)
print(m.health) 
h.give_damage()
print(m.health)

m.move(3)
s=Shark(120)
print(s.health)

