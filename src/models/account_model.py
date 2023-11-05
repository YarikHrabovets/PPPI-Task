import uuid
from typing import Union

from src.models.user_model import User


class Account:
    def __init__(self, balance: Union[int, float], user: User):
        self._account_id = uuid.uuid4()
        self._balance = balance
        self._customer = user

    def check_balance(self):
        return self._balance

    def deposit(self, amount: Union[int, float]) -> str:
        if isinstance(amount, (int, float)) and amount > 0:
            self._balance += amount
            return f'Deposit of {amount} was successful. New balance: {self._balance}'
        else:
            raise ValueError('Must be positive either int or float')

    def withdraw(self, amount: Union[int, float]) -> str:
        if not isinstance(amount, (int, float)):
            raise ValueError('Must be either int or float')
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f'Withdrawal of {amount} was successful. New balance: {self._balance}'

        return 'Insufficient funds'

