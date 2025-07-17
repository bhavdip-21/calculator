import utils.session
import unittest
from function import calculator
class Test(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(calculator.sum(3,3),6)
         
    def test_sum(self):
        self.assertEqual(calculator.sub(3,3),0)
        
        
if __name__ == '__main__':
    unittest.main()        
        
   
    