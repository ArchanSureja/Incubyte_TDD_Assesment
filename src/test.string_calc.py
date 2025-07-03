import unittest 
from string_calc import StringCalculator 

class StringCalculatorTest(unittest.TestCase):
    def test_empty_str_input(self):
        self.assertEqual(0,StringCalculator.add(""))
    
    def test_one_num_string_input(self):
        self.assertEqual(1,StringCalculator.add("1"))

    def test_two_num_string_input(self):
        self.assertEqual(3,StringCalculator.add("1,2"))
if __name__ == "__main__":
    unittest.main()

