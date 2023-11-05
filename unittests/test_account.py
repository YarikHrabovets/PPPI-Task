import unittest

from src.models.user_model import User
from src.models.account_model import Account


class TestAccountClass(unittest.TestCase):

    def setUp(self):
        user_1 = User('Antony', 18, '123 Oak Street, Springfield, IL 62701')
        user_2 = User('John', 32, '456 Pine Avenue, Rivertown, NY 10001')
        user_3 = User('Emmy', 20, '789 Maple Drive, Greenville, SC 29601')

        self.account_1 = Account(334.44, user_1)
        self.account_2 = Account(1000, user_2)
        self.account_3 = Account(4164.75, user_3)

    def test_balance(self):
        self.assertIsInstance(self.account_1.check_balance(), (int, float))
        self.assertIsInstance(self.account_2.check_balance(), (int, float))
        self.assertIsInstance(self.account_3.check_balance(), (int, float))

    def test_deposit(self):
        with self.assertRaises(ValueError):
            self.account_1.deposit('123')
        with self.assertRaises(ValueError):
            self.account_2.deposit(-0.5)

        self.assertIsInstance(self.account_3.deposit(0.25), str)
        self.assertEqual(4165, self.account_3.check_balance())

    def test_withdraw(self):
        with self.assertRaises(ValueError):
            self.account_1.withdraw('123')

        self.assertEqual('Insufficient funds', self.account_2.withdraw(0))
        self.assertEqual('Insufficient funds', self.account_2.withdraw(1001))

        self.assertIsInstance(self.account_3.withdraw(164.75), str)
        self.assertEqual(4000, self.account_3.check_balance())
