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
        super().__init__(flesh)
        super().__init__(grass)
        super().__init__(both)
        self.wild=wild
b1=Bear("grass","flesh","both","wild animal")
print(b1)



