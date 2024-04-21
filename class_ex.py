import random

class Destiny():
    classType = None
    light = 0
    elements = ['Solar', 'Arc', 'Void', 'Stasis', 'Strand', 'Prismatic']
    element = None
    
    def __init__(self, classTyp, ligh):
        self.classType = classTyp
        self.light = ligh
        #print(f'{self.classType}has risen')


    def set_element(self):
        self.element = random.choice(self.elements)
        print(f'{self.element} {self.classType}: {self.light}')
        return self.element
    
    def __del__(self):
        print(f'{self.element} {self.classType} light has faded')
        
class Relic(Destiny):
    relic_bonus = random.randint(10,20)
    def relic_power(self):
        self.light = self.light + self.relic_bonus
        print(f'Relic Level: {self.relic_bonus}')
        print(f'{self.element} {self.classType}: {self.light}')        
        
g1 = Destiny('Titan', 1810)
g1.set_element()
r1 = Relic('Titan', 1810)
r1.set_element()
r1.relic_power()

#g2 = Destiny('Hunter', 1810)
#g2.set_element()

#g3 = Destiny('Warlocks', 1810)
#g3.set_element()
