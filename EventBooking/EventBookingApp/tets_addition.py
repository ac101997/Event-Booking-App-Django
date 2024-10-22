# test_addition.py

import unittest
from addition import add

class TestAdditionFunction(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        """Test addition of two positive numbers."""
        self.assertEqual(add(3, 5), 8)

    def test_add_negative_numbers(self):
        """Test addition of two negative numbers."""
        self.assertEqual(add(-2, -4), -6)

    def test_add_positive_and_negative(self):
        """Test addition of a positive and a negative number."""
        self.assertEqual(add(7, -3), 4)

    def test_add_zero(self):
        """Test addition involving zero."""
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
