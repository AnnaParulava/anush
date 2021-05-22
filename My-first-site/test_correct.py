import unittest
import re
import main

class Test_test_3(unittest.TestCase):
    def test_A(self):
        for i in main.list_mail_cor:
         self.assertTrue((main.fun(i) is not None))
if __name__ == '__main__':
    unittest.main()