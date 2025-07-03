import unittest 
from string_calc import StringCalculator 

class StringCalculatorTest(unittest.TestCase):
    def test_empty_str_input(self):
        self.assertEqual(0,StringCalculator.add(""))
    
if __name__ == "__main__":
    unittest.main()

