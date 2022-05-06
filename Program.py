import datetime as dt


class Record:
    def __init__(self, amount, comment, date=dt.datetime.now().date()):
        self.amount = amount
        self.comment = comment
        date_format = '%d.%m.%Y'
        try:
            date = dt.datetime.strptime(date, date_format).date()
            self.date = date
        except:
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


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        total_today = self.get_today_stats()
        if total_today < self.limit:
            return (f'Сегодня можно съесть что-нибудь ещё, но с общей '
                    f'калорийностью не более {self.limit - total_today} кКал')
        else:
            return 'Хватит есть!'


class CashCalculator(Calculator):
    USD_RATE = 67.38
    EURO_RATE = 71.10

    def get_today_cash_remained(self, currency):
        total_today = self.get_today_stats()

        if currency == 'rub':
            if total_today == self.limit:
                return 'Денег нет, держись'
            elif total_today < self.limit:
                return f'На сегодня осталось {self.limit - total_today} руб'
            else:
                return (f'Денег нет, держись: '
                        f'твой долг - {total_today - self.limit} руб')
        elif currency == 'usd':
            total_today /= self.USD_RATE
            usd_limit = self.limit / self.USD_RATE
            
            if total_today == usd_limit:
                return 'Денег нет, держись'
            elif total_today < usd_limit:
                result_rnd = round(usd_limit - total_today, 2)
                return f'На сегодня осталось {result_rnd} USD'
            else:
                result_rnd = round(total_today - usd_limit, 2)
                return (f'Денег нет, держись: '
                        f'твой долг - {result_rnd} USD')
        elif currency == 'eur':
            total_today /= self.EURO_RATE
            euro_limit = self.limit / self.EURO_RATE
            
            if total_today == euro_limit:
                return 'Денег нет, держись'
            elif total_today < euro_limit:
                result_rnd = round(euro_limit - total_today, 2)
                return f'На сегодня осталось {result_rnd} USD'
            else:
                result_rnd = round(total_today - euro_limit, 2)
                return (f'Денег нет, держись: '
                        f'твой долг - {result_rnd} USD')