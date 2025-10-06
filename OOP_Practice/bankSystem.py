from abc import ABC, abstractmethod

class bank:               # Encapsulation
    def __init__(self, owner, account_id, opening_balance):
        self.owner = owner
        self.account_id = account_id
        self.opening_balance = opening_balance

    @abstractmethod       # abstraction
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

class account(bank):     # Inheritance

    def __init__(self, owner, account_id, opening_balance):
        super().__init__(owner, account_id, opening_balance)

    def withdraw(self, amount):
        if self.opening_balance <= 0:
            print(f"You don't have anything to withdraw!")
        if amount > self.opening_balance:
            print(f"You have insufficient balance!")  
        self.opening_balance -= amount

    def deposit(self, amount):
        if self.opening_balance > 0:
            self.opening_balance += amount
        if self.opening_balance <= 0:
            self.opening_balance = amount

account_holder = account("Sad", "S-432", 500)