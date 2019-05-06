import unittest

from cough import cough

class Test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(cough(3), 'cough cough cough ')
    def test_case2(self):
        self.assertEqual(cough(1), 'cough ')

if __name__ =="__main__":
    unittest.main()