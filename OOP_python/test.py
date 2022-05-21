class LightSwitch():
    
    isOn = False
    def __init__(self,name):
        self.name = name
    
    def toggle(self):
        self.isOn = not self.isOn
        print('the ' + self.name + ' is on: ' + str(self.isOn))

class GarbageSwitch(LightSwitch):
    pass



    


lo1 = LightSwitch("kitcken light")
lo2 = LightSwitch("Bedroom light")
go = GarbageSwitch("garbage disposle")
lo1.toggle()
lo2.toggle()
go.toggle()