# CONSTUCTOR OVERLOADING WITH DEFAULT PARAMETERS
#Constructor overloading means using the same constructor name to perform different actions
#based on the arguments passed.
#Python does not support multiple constructors. So, constructor overloading is achieved by 
#using a single constructor with default parameters (commonly None).
#While creating objects, different arguments are passed, which changes the behavior of the 
#constructor for each object.
# WHILE OBJECT CREATION , THE CONSTRUCTOR IS OVERLOADED USING DIFFERENT ARGUMENTS.
class Person:
    def __init__(self,name="Anushka",age=None,address=None):
        self.name=name
        self.age=age
        self.address=address
p=Person(age=22)
print(p.name)
print(p.age)
p2=Person(address="new colony")
print(p2.name,p2.age,p2.address)