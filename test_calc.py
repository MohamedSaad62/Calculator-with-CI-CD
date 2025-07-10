import unittest
from calc import calculate  # 👈 updated import

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate(2, '+', 3), 5)
        self.assertEqual(calculate(2, '+', 5), 7)


    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculate(1, '-', 1)

if __name__ == "__main__":
    unittest.main()
