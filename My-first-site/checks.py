
import re, datetime
from datetime import datetime

class input_check:
    # метод для проверки почты
    def author_email_correct(email):    
        regex = re.compile(r"^\w+@\w+(\.\w+)+$") # проверка регулярным выражением
        if re.match(regex, email):
            return True



