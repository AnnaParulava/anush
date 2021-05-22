
#import unittest, re, checks

#class AssertFalseTest(unittest.TestCase):
#    def test_A(self):
#        for j in emails.list_mail_uncor:
#            self.assertFalse((emails.fun(j)))
#if __name__ == '__main__':
#    unittest.main()


import unittest, re, checks

class AssertFalseTest(unittest.TestCase):

    def test_realEmails(self):
        list_mail_cor = ['some@mail', 'some@mail.', '@mail.ru',
                         'incorrectMail@@mailCheck.point', 'user@mail.ru@',
                         '@user@mail.ru', 'username@mail.n', 'user@mail.russ'
                         'user.@mail.ru', 'user@mail..ru', 'user@mail.ru.']
        for mail in list_mail_cor:
            self.assertFalse(checks.input_check.author_email_correct(mail))

if __name__ == '__main__':
    unittest.main()

    
