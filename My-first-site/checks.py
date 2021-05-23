
import unittest
import re
from datetime import datetime

list_mail_uncor = ["1","wrw@ksjf...ksu","jhg.sds.dsf","","jsghfa"]
list_mail_cor = ["m.m@mail.ru", "m1@gmail.com","131m@mail.com","jjjjj@qwe.ds", "ap55@yandex.com"]
re_mail=r"^\w+@\w+(\.\w+)+$"
re_date = r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$"

def author_email_correct(email):
    return re.match(re_mail,email) is not None

def written_date_correct(date_input):
        if re.match(re_date, date_input) is None:
            return False
        try:
            # перевод строки в datatime
            date = datetime.strptime(date_input, '%Y-%m-%d')
            # проверка того, что введенная дата не больше текущей
            if date <= datetime.today():
                return True
            else: return False
        except ValueError:
            return False