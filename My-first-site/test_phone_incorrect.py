import unittest
import re
import checks

class Test_test_phone_cor(unittest.TestCase):
    def test_A(self):
        for i in checks.list_phone_uncor:
            self.assertFalse(checks.author_phone(i))
if __name__ == '__main__':
    unittest.main()


