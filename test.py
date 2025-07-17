import unittest
from function import calculator
class Test(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(calculator.sum(3,3),6)
        
        
        
        
   
    