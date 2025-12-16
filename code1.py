class Laptop:
    storage_type="ssd"
    def __init__(self,RAM,storage):
        print("constructor is called")
        self.RAM=RAM
        self.storage=storage
    def get_info(self):       #instance method
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")
    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")
    @staticmethod
    def calc_discount(price,discount):
        return f"final_price = {price - (price*discount)/100}"
l1=Laptop("16gb","512gb")
l1.get_info()
l1.get_storage_type()
Laptop.get_storage_type()
print(l1.calc_discount(40_000,10))
l1.calc_discount(40_000,10)

