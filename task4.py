# Custom Exception
class InsufficientFundsError(Exception):
    pass

# Parent Class
class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount} -> balance {self.balance}") 

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Insufficient funds: balance {self.balance}, requested {amount}")

        self.balance -= amount
        print(f"{self.owner} withdraw {amount} -> balance {self.balance}")

    # Bonus Challenge
    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.balance}"

# Child Class (Inheritance)
class SavingsAccount(Account):
    def __init__(self, owner, balance=0, min_balance=500):
        super().__init__(owner, balance)
        self.min_balance = min_balance

    # Method Overriding
    def Withdraw(self, amount):

        if self.balance - amount < self.min_balance:
             raise InsufficientFundsError(f"Insufficient funds: balance {self.balance}, requested {amount}")


        self.balance -= amount
        print(f"{self.owner} withdraw {amount} -> balance {self.balance}")

# Create Savings Account
kishore = SavingsAccount("kishore",  1500) 

# First Withdrawal
try:
    kishore.withdraw(1200) 

except InsufficientFundsError as e:
    print("Error:", e)

# Second Withdrawal
try:
    kishore.withdraw(800)

except InsufficientFundsError as e:
    print("Error:", e) 

# Check Inheritance
print(isinstance(kishore, Account)) 

# Bonus Challenge Output
print(kishore)




        

