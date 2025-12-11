#Create a **BankAccount** class that stores an account number, owner name, and balance, and includes methods to **deposit money**, **withdraw money**, and **check the current balance**.
class BankAccount:
    def __init__(self, account_no, owner_name, balance):
        print("constructor is called")
        self.account_no = account_no
        self.owner_name = owner_name
        self.balance = balance
        print(f"Account created for {self.owner_name} with account number {self.account_no} and initial balance {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: {amount}"

    def withdraw(self, amount):
        self.balance -= amount
        return f"Withdrawn: {amount}"

    def check_balance(self):
        return f"Current balance: {self.balance}"

b = BankAccount(77890, "anush", 2000)
print(b.deposit(500))
print(b.withdraw(300))
print(b.check_balance())
