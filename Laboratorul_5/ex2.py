class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Current balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds. Cannot withdraw.")

    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    def calculate_interest(self):
        interest_rate = 0.02
        interest = self.balance * interest_rate
        self.balance += interest
        print(f"Interest added: ${interest:.2f}. New balance: ${self.balance:.2f}")

class CheckingAccount(Account):
    def calculate_interest(self):
        print("Checking accounts do not earn interest.")

savings = SavingsAccount(account_number="SA123", balance=1000)
savings.deposit(500)
savings.withdraw(200)
savings.calculate_interest()

checking = CheckingAccount(account_number="CA456", balance=2000)
checking.deposit(300)
checking.withdraw(250)
checking.calculate_interest()
