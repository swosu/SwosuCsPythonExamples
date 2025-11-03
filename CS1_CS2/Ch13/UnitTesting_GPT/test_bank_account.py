# test_bank_account.py
import unittest
from bank_account import BankAccount  

class TestBankAccount(unittest.TestCase):
    def test_initial_balance(self):
        account = BankAccount()
        self.assertEqual(account.get_balance(), 0)

    def test_deposit(self):
        account = BankAccount()
        account.deposit(100)
        self.assertEqual(account.get_balance(), 100)

if __name__ == "__main__":
    unittest.main()
