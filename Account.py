class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance


    def deposit(self, amount):
        """Base withdraw method can be overwritten by the subclasses"""
        if amount > 0:
            self.__balance += amount
            print(f"Deposit of {amount} successful. New balance: {self.__balance}")
        else:
            print("Deposit amount must be a positive number.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.__balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient Funds")

    def get_balance(self):
        return self.__balance