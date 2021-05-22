import unittest
import re

list_mail_uncor = ["1","wrw@ksjf...ksu","jhg.sds.dsf","","jsghfa"]
list_mail_cor = ["m.m@mail.ru", "m1@gmail.com","131m@mail.com","jjjjj@qwe.ds", "ap55@yandex.com"]
re_mail=r"^\w+@\w+(\.\w+)+$"

def fun(i):
    return re.match(re_mail,i) is not None