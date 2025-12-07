class BankAccount:
    def __init__(self,name , balance):
        print("constructor is called")
        self.name = name
        self.__balance = balance               #private attribute
    def get_balance(self):                     #getter method
        return self.__balance   
    def set_balance(self,new_balance):         #setter method
        self.__balance=new_balance 
        return self.__balance
acc1 = BankAccount("Rahul Kumar", 10_000)
print(acc1.name, acc1.get_balance())
print(f"{acc1.name} has balance = {acc1.get_balance()}")
print(f"New balance updated through set_ method = {acc1.set_balance(20_000)}")
print(f"{acc1.name} has balance = {acc1.get_balance()}")
print(acc1.name, acc1._BankAccount__balance)

#class BankAccount:
#    def __init__(self,name , balance):
#        print("constructor is called")
#        self.name = name
#        self.__balance = balance               #private attribute
#    def get_balance(self):                     #getter method
#        return self.__balance    
#acc1 = BankAccount("Rahul Kumar", 10_000)
#print(acc1.name, acc1.get_balance())
#print(f"{acc1.name} has balance = {acc1.get_balance()}")

#class BankAccount:
#    def __init__(self,name , balance):
#        print("constructor is called")
#        self.name = name
#        self._balance = balance               #protected attribute
#acc1 = BankAccount("Rahul Kumar", 10_000)
#print(acc1.name,acc1._balance)
#print(f"{acc1.name} has balance = {acc1._balance}")
