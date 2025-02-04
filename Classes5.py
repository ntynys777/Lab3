class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Deposits the specified amount to the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """Withdraws the specified amount if sufficient balance exists."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

account = BankAccount("John Doe", 100)
account.deposit(50)  
account.withdraw(30)  
account.withdraw(200)  
