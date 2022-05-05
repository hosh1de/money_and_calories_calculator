import datetime as dt


class Record:
    def __init__(self, amount, comment, date=dt.datetime.now().date()):
        self.amount = amount
        self.comment = comment
        try:
            date = str(date.strftime('%d.%m.%Y'))
        except:
            pass
        date_format = '%d.%m.%Y'
        date = dt.datetime.strptime(date, date_format).date()
        self.date = date


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        temp = []

        temp.append(record.amount)
        temp.append(record.comment)
        temp.append(record.date)

        self.records.append(temp)

    def get_today_stats(self):
        date = dt.datetime.now().date()
        total = 0
        for data in self.records:
            if data[2] == date:
                total += data[0]
        return total

    def get_week_stats(self):
        date = dt.datetime.now().date()
        total = 0
        period = dt.timedelta(days=7)
        delta = date - period
        for data in self.records:
            if data[2] > delta:
                total += data[0]
        return total


# class CaloriesCalculator(Calculator):
#     def get_calories_remained():



calculator = Calculator(1000)
calculator.add_record(Record(amount=145, comment="кофе"))
calculator.add_record(Record(amount=300, comment="Серёге за обед"))
calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
r4 = calculator.get_week_stats()
r5 = calculator.get_today_stats()
print()