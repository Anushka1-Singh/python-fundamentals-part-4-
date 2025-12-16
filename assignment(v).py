class Vehicle:  
    print("base class vehicle called")
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def intro(self):
        print(self.brand,self.model)
class Car(Vehicle):
    def __init__(self,brand,model,seats):
        super().__init__(brand,model)
        self.seats=seats
    def info1(self):
        print(self.model,self.brand,self.seats)
class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc
    def info2(self):
        print(self.model,self.brand,self.engine_cc)
v1 = Vehicle("ford","120a")
v1.intro()
v2=Car("tesla","234",5)
v2.info1()
v3=Bike("thar", "456" ,23000)
v3.info2()