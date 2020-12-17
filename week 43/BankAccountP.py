# Problem 8.4. Extending the BankAccountP class

class BankAccountP2:
    def __init__(self, first_name, last_name, number, balance):
        self._first_name = first_name
        self._last_name = last_name
        self._number = number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):    # NEW - read balance value
        return self._balance

    def print_info(self):
        first = self._first_name; last = self._last_name
        number = self._number; bal = self._balance
        s = f'{first} {last}, {number}, balance: {bal}'
        print(s)

    def transfer(self, other_account, amount):
        self._balance -= amount
        other_account._balance += amount


konto1 = BankAccountP2('Navn', 'Navnesen', 123456789, 1000)
konto2 = BankAccountP2('Navn2', 'Navnesen', 234567890, 1000)

konto1.transfer(konto2, 100)

print(konto1.get_balance()) # should give 900
print(konto2.get_balance()) # should give 1100

"""

printed:
900
1100

"""
