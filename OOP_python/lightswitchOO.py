#OO lightswitch

class LightSwitch():
    def __init__(self, name):
        self.isSwitchOn = False
        self.name = name

    def check(self):
        print("the " + self.name + " light is " + str(self.isSwitchOn))
        
k=LightSwitch("kitchen")
br=LightSwitch("bathroom")
k.check()
br.check()