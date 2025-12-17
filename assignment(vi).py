class Herbivore:
    def __init__(self,grass):
        self.grass=grass 
    def info(self):
        print("eats",self.grass)
class Carnivore:
    def __init__(self,flesh):
        self.flesh=flesh
    def action(self):
        print("skin meat",self.flesh)
class Omnivore:
    def __init__(self,both):
        self.both=both
    def work(self):
        print("grass and flesh",self.both)
class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, grass, flesh, both, wild):
        Herbivore.__init__(self,grass)
        Carnivore.__init__(self,flesh)
        Omnivore.__init__(self,both)
        self.wild=wild
b1=Bear("grass","flesh","both","wild animal")
print(b1.grass,b1.flesh,b1.both,b1.wild)
b1.info()
b1.action() 
b1.work()



