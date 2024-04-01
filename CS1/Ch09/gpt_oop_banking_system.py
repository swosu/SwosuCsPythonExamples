"""
creating a basic banking system 
that allows users to create accounts, 
deposit money, 
withdraw money, and 
check their balance.

Here's a breakdown of what you need to do:

Create a class called BankAccount to represent a bank account. It should have the following attributes:

Account holder's name
Account number (which can be generated automatically)
Current balance
Implement methods for the following actions:

Creating an account
Depositing money
Withdrawing money
Checking the account balance
Write a simple program that allows users to interact with the banking system:

Prompt the user to create an account or perform other actions (deposit, withdraw, check balance)
Based on the user's input, perform the appropriate action on the account.
"""

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.account_number = self.generate_account_number()

    def generate_account_number(self):
        import random
        return random.randint(100000, 999999)

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

    def check_balance(self):
        return self.balance