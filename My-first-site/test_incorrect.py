import unittest
import re
import main

class Test_test_incorrect(unittest.TestCase):
    def test_A(self):
        for j in main.list_mail_uncor:
            self.assertFalse((main.fun(j)))
if __name__ == '__main__':
    unittest.main()