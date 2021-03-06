import datetime as dt


class Record:
    """Create a record of spending money or calories"""

    def __init__(self, amount, comment, date=dt.datetime.now().date()):
        """
        Initialize the Record class

        Key arguments:
        amount -- amount of money or the number of calories (required)
        comment -- explanation of what the money was spent on or where 
        the calories came from (required)
        date -- date the record was created (default today date)

        Restrictions:
        1. the amount argument must be non-negative
        2. a future date is possible
        """

        self.amount = amount
        self.comment = comment

        if isinstance(date, str):
            date_format = '%d.%m.%Y'
            date = dt.datetime.strptime(date, date_format).date()

        self.date = date


class Calculator:
    """Create a parent class for entering the date and counting wastes"""

    def __init__(self, limit):
        """
        Initialize the Calculator class

        Key arguments:
        limit -- daily spending limit set by the user (required)

        Restrictions:
        1. the limit argument must be non-negative
        """
        
        self.limit = limit
        self.records = []

    def add_record(self, record):
        """
        Add an entry to the class list

        Key arguments:
        record -- a record of spending money or calories (required)

        Restrictions:
        1. the record argument must be of the Record class
        """

        self.records.append(record)

    def get_days_ago_stats(self, days):
        """
        Get the number of expenses for a certain number of days

        Key arguments:
        days -- The number of days you need to get statistics (required)

        Restrictions:
        1. the days argument must be non-negative
        """

        today = dt.datetime.now().date()
        delta = dt.timedelta(days=days)
        days_ago = today - delta

        days_count = sum(rec.amount for rec in self.records 
                         if days_ago <= rec.date <= today)

        return days_count

    def get_today_stats(self):
        """Get the sum of all expenses for today"""

        today_count = self.get_days_ago_stats(0)
        return today_count

    def get_week_stats(self):
        """Get the amount of expenses for the last 7 days"""

        week_count = self.get_days_ago_stats(7)
                         
        return week_count


class CaloriesCalculator(Calculator):
    """
    ??reate a child class to determine the remaining calories
    
    Behaviour:
    All methods of the parent class remain 
    """

    def get_calories_remained(self):
        """Determine whether it is possible to get calories today"""

        today_count = self.get_today_stats()
        
        if today_count < self.limit:
            left_calories = self.limit - today_count
            return (f'?????????????? ?????????? ???????????? ??????-???????????? ??????, ???? ?? ?????????? '
                    f'?????????????????????????? ???? ?????????? {left_calories} ????????')
        
        return '???????????? ????????!'


class CashCalculator(Calculator):
    """
    ??reate a child class to determine how much money is left in a 
    certain currency today
    
    Behaviour:
    All methods of the parent class remain 
    """

    USD_RATE = 67.38
    EURO_RATE = 71.10
    RUB_RATE = 1.0

    def get_today_cash_remained(self, currency):
        """
        Determine the balance of money for today and make a conclusion

        Key arguments:
        currency -- the currency in which we will transfer money (required)

        Restrictions:
        1. the currency argument must be equal to 'rub', 'usd' or 'eur'
        """

        today_count = self.get_today_stats()
        
        if today_count == self.limit:
            return '?????????? ??????, ??????????????'

        currencies = {
            'rub': ('??????', self.RUB_RATE),
            'usd': ('USD', self.USD_RATE),
            'eur': ('Euro', self.EURO_RATE),
        }

        currency_name, currency_rate = currencies.get(currency)
        remained_cash = abs(self.limit - today_count)
        remained_cash_in_currency = round((remained_cash / currency_rate), 2)

        if today_count < self.limit:
            return (f'???? ?????????????? ???????????????? '
                    f'{remained_cash_in_currency} {currency_name}')

        return (f'?????????? ??????, ??????????????: '
                f'???????? ???????? - {remained_cash_in_currency} {currency_name}')