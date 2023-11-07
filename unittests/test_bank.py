import unittest

from src.models.user_model import User
from src.models.account_model import Account
from src.models.bank_model import Bank


class TestBankClass(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()
        self.user_1 = User('Antony', 18, '123 Oak Street, Springfield, IL 62701')

    def test_get_account(self):
        self.bank.accounts = {'1a2b3c': Account(1000, self.user_1)}

        self.assertEqual('Account does not exist', self.bank.get_account(Account(334.44, self.user_1).account_id))
        self.assertEqual(self.bank.accounts['1a2b3c'], self.bank.get_account('1a2b3c'))

    def test_create_account(self):
        with self.assertRaises(TypeError):
            self.bank.create_account('1', 2, '3', 4, 5)
        with self.assertRaises(ValueError):
            self.bank.create_account(1, 2, '3', 4)

        account_1 = self.bank.create_account('John', 32, '456 Pine Avenue, Rivertown, NY 10001', 1000)
        account_2 = self.bank.create_account('Emmy', 20, '789 Maple Drive, Greenville, SC 29601', 4164.75)

        self.assertEqual(account_1, self.bank.get_account(account_1.account_id))
        self.assertEqual(account_2, self.bank.get_account(account_2.account_id))

    def test_delete_account(self):
        account_1 = Account(1000, self.user_1)
        account_2 = self.bank.create_account('Emmy', 20, '789 Maple Drive, Greenville, SC 29601', 4164.75)
        account_3 = self.bank.create_account('John', 32, '456 Pine Avenue, Rivertown, NY 10001', 1000)

        self.assertEqual(False, self.bank.delete_account(account_1.account_id))
        self.assertEqual(True, self.bank.delete_account(account_2.account_id))
        self.assertEqual('Account does not exist', self.bank.get_account(account_2.account_id))
        self.assertEqual(True, self.bank.delete_account(account_3.account_id))
        self.assertEqual('Account does not exist', self.bank.get_account(account_3.account_id))
