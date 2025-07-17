import unittest

class Test(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(sum(3,3),6)