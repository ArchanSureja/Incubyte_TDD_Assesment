import unittest 
from string_calc import StringCalculator , NegetiveNumberException

class StringCalculatorTest(unittest.TestCase):
    def test_empty_str_input(self):
        self.assertEqual(0,StringCalculator.add(""))
    
    def test_one_num_string_input(self):
        self.assertEqual(1,StringCalculator.add("1"))

    def test_two_num_string_input(self):
        self.assertEqual(3,StringCalculator.add("1,2"))
    
    def test_multiple_num_string_input(self):
        self.assertEqual(10,StringCalculator.add("1,2,3,4"))
    
    def test_newline_delimeter(self):
        self.assertEqual(6,StringCalculator.add("1\n2,3"))
        self.assertEqual(7,StringCalculator.add("5\n2"))
        self.assertEqual(11,StringCalculator.add("5\n1\n5"))
    
    def test_custom_delimeter(self):
        self.assertEqual(3,StringCalculator.add("//;\n1;2"))
        self.assertEqual(4,StringCalculator.add("//;\n1;2;1"))
    
    def test_negetive_number_input(self):
        try:
            StringCalculator.add("-1")
        except NegetiveNumberException as e:
            self.assertEqual("negetive numbers not allowed -1",str(e))
        try:
            StringCalculator.add("-1,-2,3")
        except NegetiveNumberException as e:
            self.assertEqual("negetive numbers not allowed -1, -2",str(e))
        
if __name__ == "__main__":
    unittest.main()

