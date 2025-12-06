class Products:
    name = "electronic device"
    price= 100
    track =0
    def __init__(self,name,price):
        print("constructor is called")
        self.name=name
        self.price=price
        Products.track += 1
    @classmethod
    def list_products(cls):
        print(f"Total products created: {cls.track}")
    @staticmethod
    def discount_products(price, discount):
        disc = price*discount/100
        return f"discount amount ={disc}"
p1=Products("laptop",50_000)
p2=Products("phone",20_000)
p3=Products("tavlet",15_000)
print(p1.name,p1.price)
print(p2.name,p2.price)
Products.list_products()
print(p1.discount_products(p1.price, 10))



        
        