from bottle import post, request
import re
import pdb


#Паттерн для проверки адреса электронной почты 
@post('/home', method='post')
def my_form():
    user_requests = {}
   # mail = request.forms.get('ADRESS')
   # question = request.forms.get('QUEST')
    question="Hello! Сan I get a job with you?"
    mail="ap554156@gmail.com"

    if((mail=='')|(question=='')):
        return "Please, put all information"
    else:
        if(re.match(r"^\w+@\w+(\.\w+)+$", mail)):
          # mail = request.forms.get('ADRESS')
          # user_requests[mail] = question
          # pdb.set_trace()
          # return "Thanks! The answer will be sent to the mail %s" % mail    
           test=True
           return test
        else:
           # return "Please, put a correct email (like www@mail.com)"
            test=False
            return test
