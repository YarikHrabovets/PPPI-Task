import unittest
from src.models.user_model import User


class TestUserClass(unittest.TestCase):

    def setUp(self):
        self.user_1 = User('Antony', 18, '123 Oak Street, Springfield, IL 62701')
        self.user_2 = User('John', 32, '456 Pine Avenue, Rivertown, NY 10001')
        self.user_3 = User('Emmy', 20, '789 Maple Drive, Greenville, SC 29601')

    def test_name(self):
        with self.assertRaises(ValueError):
            self.user_1.name = 22
        with self.assertRaises(ValueError):
            self.user_2.name = 'Ab'
        with self.assertRaises(ValueError):
            self.user_3.name = 'Abram11'

        self.user_3.name = 'Ryan'
        self.assertEqual('Ryan', self.user_3.name)

    def test_age(self):
        with self.assertRaises(ValueError):
            self.user_1.age = '30'
        with self.assertRaises(ValueError):
            self.user_2.age = 0

        self.user_3.age = 30
        self.assertEqual(30, self.user_3.age)

    def test_address(self):
        with self.assertRaises(ValueError):
            self.user_1.address = 0
        with self.assertRaises(ValueError):
            self.user_2.address = '1234 Wrong, address, SC 43091'

        self.user_3.address = '11 Elm Street, Fallfield, IL 62701'
        self.assertEqual('11 Elm Street, Fallfield, IL 62701', self.user_3.address)
