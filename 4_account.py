import pytz
from datetime import datetime

WHITE = '\033[00m'
GREEN = '\033[0;92m'
RED = '\033[1;31m'


class Account:
    def __init__(self, name, balance):
        self.name = name
        # Во время компиляции , в байт код имя станет _Account__balance
        # И мы не сожем поменять баланс так: a.__balance = 10000000
        # Новое свойство __balance просто добавится в a.__dict__
        self.__balance = balance
        self._history = []

    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.utcnow())

    def deposit(self, amount):
        self.__balance += amount
        self.show__balance()
        self._history.append([amount, self._get_current_time()])

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f'You spent {amount} units')
            self.show__balance()
            self._history.append([-amount, self._get_current_time()])
        else:
            print('Not enough money')
            self.show__balance()

    def show__balance(self):
        print(f'Balance: {self.__balance}')

    def show_history(self):
        for amount, date in self._history:
            if amount > 0:
                transaction = 'deposited'
                color = GREEN
            else:
                transaction = 'withdraw'
                color = RED
            print(f'{color} {amount} {WHITE} {transaction} on {date.astimezone()}')


a = Account('artem', 0)

a.deposit(578)
a.withdraw(87)
a.deposit(234)
a.show_history()
a.__balance = 1000000
a.show__balance()
print(a.__dict__)
print(a._history)
