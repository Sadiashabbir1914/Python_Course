from abc import ABC, abstractmethod

import csv

class Account(ABC):           # Abstract Base Class

    def __init__(self, owner, account_no, balance):    # initializar constructor
        self.owner = owner
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount) -> int:           # for depositing money
        self.balance += amount
        return f"Your current balance is Rs. {self.balance}."

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def monthly_process(self):
        pass

class SavingAccount(Account):

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

class CurrentAccount(Account):

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

    def add(self, account: Account):               # adding accounts into Account object
        self.accounts[account.account_no] = account

    def get(self, account_no):                     # returning account_no from accounts
        return self.accounts[account_no]
    
    def transfer(self, account_no_from, account_no_to, amount):
        sender = self.get(account_no_from)
        receiver = self.get(account_no_to)

        sender.withdraw(amount)
        receiver.deposit(amount)

    def load_from_csv(self, file = "accounts_updated.csv"):

        with open(file, "r") as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                account_type = row.get("Account_type") or ""
                acc_owner = row.get("owner") or ""
                acc_no = row.get("account_no") or ""
                acc_balance = row.get("balance") or ""
                rate = row.get("interest_rate") or ""
                limit = row.get("loan_limit") or ""
                fee = row.get("fees") or ""

                if account_type == "saving":
                    acc = SavingAccount(acc_owner, acc_no, acc_balance, rate)
                elif account_type == "current":
                    acc = CurrentAccount(acc_owner, acc_no, acc_balance, limit, fee)
                else:
                    raise ValueError ("Invalid account!")
            
            self.add(acc)


    def save_to_csv(self, file = "accounts_updated.csv"):

        header = ["Account_type", "owner", "account_no", "balance", "interest_rate", "loan_limit", "fees"]

        with open(file,"w") as f:
            writer = csv.writer(f)
            writer.writerow(header)

            for acc in self.accounts.values():
                if isinstance(acc, SavingAccount):
                    writer.writerow(["saving", acc.owner, acc.account_no, acc.balance])
                elif isinstance(acc, CurrentAccount):
                    writer.writerow(["current", acc.owner, acc.account_no, acc.balance, acc.loan_limit, acc.fees])
                else:
                    writer.writerow(["", acc.owner, acc.account_no, acc.balance, acc.interest_rate])

    def show_acc(self, file = "accounts_updated.csv"):

        with open(file, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                print(row)

    def show(self):

        for i in self.accounts:
            print(f"Account Number: {i}")

    def options(self):

        print("Enter 1 to add an account. ")
        print("Enter 2 to Load account no. ")
        print("Enter 3 to show all accounts. ")
        print("Enter 4 to exit. ")

        n = int(input("Enter your choice: "))

        if n == 1:
            bank.add(acc2)
        elif n == 2:
            bank.show()
        elif n == 3:
            bank.show_acc()
        elif n == 4:
            exit
        else:
            print("Invalid Choice!")

bank = Bank("Standard Charted Bank")
acc1 = SavingAccount("Sadia", "S-432", 500, 50)
acc2 = CurrentAccount("Shabir", "F-322", 1000, 500, 10)
bank.add(acc1)
bank.add(acc2)
acc1.deposit(1500)
bank.get("S-432").deposit(500)
bank.transfer("S-432", "F-322", 1000)
bank.load_from_csv("accounts_updated.csv")
bank.save_to_csv("accounts_updated.csv")
bank.options()