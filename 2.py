class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Invalid withdrawal amount")
        else:
            self.__balance -= amount
            print("Withdrawal successful")


account = BankAccount(10000)
print("Balance:", account.balance)
account.deposit(5000)
print("Balance:", account.balance)
account.withdraw(3000)
print("Balance:", account.balance)
account.withdraw(20000)