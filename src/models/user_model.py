import re


class User:
    street_address_pattern = r'^\d+\s+\w+\s+\w+,\s+\w+,\s+\w+\s+\d+\d+$'

    def __init__(self, name: str, age: int, address: str):
        self._name = name
        self._age = age
        self._address = address

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and len(value) >= 3 and value.isalpha():
            self._name = value
        else:
            raise ValueError('Value must be a string and more or equal 3 characters')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: int):
        if isinstance(value, int) and value > 17:
            self._age = value
        else:
            raise ValueError('Value must be an integer and greater than 17')

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value: str):
        if isinstance(value, str) and re.match(self.street_address_pattern, value):
            self._address = value
        else:
            raise ValueError('Provide correct address')
