from src.models.account_model import *


def accepts(*types):
    def check_accepts(f):
        if len(types) != f.__code__.co_argcount - 1:
            raise TypeError('Wrong length of arguments')

        def new_f(*args, **kwargs):
            for (a, t) in zip(args[1:], types):
                if not isinstance(a, t):
                    raise ValueError(f'arg {a} does not match {t}')
            return f(*args, **kwargs)

        new_f.__name__ = f.__name__
        return new_f

    return check_accepts


class Bank:
    def __init__(self):
        self.accounts = {}

    def get_account(self, account_id: str) -> Union[Account, str]:
        return self.accounts.get(account_id, 'Account does not exist')

    @accepts(str, int, str, (int, float))
    def create_account(self, name: str, age: int, address: str, balance: Union[int, float] = 0) -> Account:
        user = User(name, age, address)
        account = Account(balance, user)
        self.accounts[account.account_id] = account

        return account

    def delete_account(self, account_id: str) -> bool:
        try:
            del self.accounts[account_id]
            return True
        except KeyError:
            return False
