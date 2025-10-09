from abc import ABC, abstractmethod

import csv

class account(ABC):           # Abstract Base Class

    def __init__(self, owner, account_no, balance):    # initializar constructor
        self.owner = owner
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):           # for depositing money
        self.balance += amount
        return f"Your current balance is Rs. {self.balance}."

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def monthly_process(self):
        pass

class saving_account(account):

    def __init__(self, owner, account_no, balance, interest_rate):
        super().__init__(owner, account_no, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if self.balance <= amount:
            return(f"You entered insufficient balance!")
        self.balance -= amount
    
    def monthly_process(self):              # adding interest on accounts
        interest = (self.balance * self.interest_rate) / 12
        self.balance += interest

class current_account(account):
    def __init__(self, owner, account_no, balance, loan_limit, fees):
        super().__init__(owner, account_no, balance)
        self.loan_limit = loan_limit
        self.fees = fees

    def withdraw(self, amount):
        if self.balance < amount:
            return(f"You entered insufficient balance!")
        if self.balance - amount <= -self.loan_limit:
            return("Your loan limit has exceeded!")
        self.balance -= amount

    def monthly_process(self):
        if self.balance < 0:
            self.balance -= self.fees

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def add(self, Account: account):               # adding accounts into Account object
        self.accounts[Account.account_no] = Account

    def get(self, account_no):                     # returning account_no from accounts
        return self.accounts[account_no]
    
    def transfer(self, account_no_from, account_no_to, amount):
        sender = self.get(account_no_from)
        receiver = self.get(account_no_to)

        sender.withdraw(amount)
        receiver.deposit(amount)

    def load_from_csv(self, file = "accounts.csv"):
        with open(file, "r") as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                print(row)

    def save_to_csv(self, file = "accounts_updated.csv"):
        with open(file, "w") as f:
            writer = csv.DictWriter(f)
            writer.writeheader()

            for acc in self.accounts: 
                account_obj = self.accounts[acc]
                writer.writerow({
                "Account_type": account_obj.__class__.__name__,
                "owner": account_obj.owner,
                "account_no": account_obj.account_no,
                "balance": account_obj.balance})

    def show(self):
        for i in self.accounts:
            print(i)
    
bank = Bank("Standard Charted Bank")
bank.load_from_csv("accounts.csv")
bank.show()
bank.get("S-123").deposit(500)
bank.transfer("F-321", "S-123", 100)
bank.save_to_csv("accounts_updated.csv")