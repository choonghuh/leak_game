# To run a single test, ex) python -m unittest test_simple.SimpleTestCase.test_add

import unittest

# Simple function to be tested
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

# Test cases
class SimpleTestCase(unittest.TestCase):
    
    def test_add(self):
        """Test the add function"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        """Test the subtract function"""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        """Test the multiply function"""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 10), 0)

# This allows the tests to be run from the command line
if __name__ == '__main__':
    unittest.main()
