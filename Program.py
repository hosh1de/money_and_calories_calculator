import datetime as dt


class Record:
    def __init__(self, amount, comment, date = dt.date.today()):
        self.amount = amount
        self.comment = comment
        self.date = date

    def __str__(self):
        return f'{self.amount}, {self.comment}, {self.date}'


r1 = Record(amount=145, comment="Безудержный шопинг", date="08.03.2019")
r2 = Record(amount=1568, comment="Наполнение потребительской корзины")


print(r1)
print(r2)
