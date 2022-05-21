#tv class

class TV():
    def __init__(self,brand,location):
        self.isOn = False
        self.isMuted = False
        self.channelList = [2,4,5,7,9,11,20,56]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0
        self.VOLUME_MAXIMUM = 10
        self.volume = self.VOLUME_MAXIMUM
        self.brand = brand
        self.location = location

    def power(self):
        self.isOn = not self.isOn
        print('toggled')
        print(self.isOn)
    
    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1
    
    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume - 1
    
    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex > self.nChannels:
            self.channelIndex = 0

    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex - 1
        if self.channelIndex < 0:
            self.channelIndex = self.channelIndex - 1

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)
    
    def showInfo(self):
        print()
        print('TV status :', self.brand)
        if self.isOn:
            print('    Location: ',self.location)
            print('    TV is: On')
            print('    Channel is: ', self.channelList[self.channelIndex])
            if self.isMuted:
                print('    Volume is: ', self.volume, '(sound is muted)') 
            else:
                print('    Volume is: ', self.volume)
        else:
            print('    TV is: OFF')

o = TV('Sony','bedroom')
o2 = TV("vizio", 'living room')
o.showInfo()
o.power()
o.showInfo()
o.channelUp()
o.channelUp()
o.volumeDown()
o.volumeDown()

o.showInfo()
o.power()
o.showInfo()
o2.showInfo()