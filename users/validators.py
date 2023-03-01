
import datetime
from django.core.exceptions import ValidationError
from dateutil.relativedelta import relativedelta


def delta_date(value):
    age = relativedelta(datetime.date.today(), value).years
    if age < 9:
        raise ValidationError(f"Registration is prohibited your age is {age} years old,"
                              f" you are under 9 years old")


def not_rambler(value):
    if "rambler.ru" in value:
        raise ValidationError("email cannot be created in the 'rambler.ru' domain")
