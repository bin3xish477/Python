import unittest
import math_operations

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(math_operations.add(10, 5), 15)
        self.assertEqual(math_operations.add(-1, 1), 0)
        self.assertEqual(math_operations.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(math_operations.subtract(10, 5), 5)
        self.assertEqual(math_operations.subtract(-1, 1), -2)
        self.assertEqual(math_operations.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(math_operations.multiply(10, 5), 50)
        self.assertEqual(math_operations.multiply(-1, 1), -1)
        self.assertEqual(math_operations.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(math_operations.divide(10, 5), 2)
        self.assertEqual(math_operations.divide(-1, 1), -1)
        self.assertEqual(math_operations.divide(-1, -1), 1)

        # self.assertRaises(
        #     ZeroDivisionError,
        #     math_operations.divide, 10, 0
        # )

        # same as commented out code above
        with self.assertRaises(ZeroDivisionError):
            math_operations.divide(10, 0)

    def test_mod(self):
        self.assertEqual(math_operations.mod(10, 5), 0)
        self.assertEqual(math_operations.mod(50, 8), 2)
        self.assertNotEqual(math_operations.mod(10, 3), 2)

if __name__ == "__main__":
    unittest.main()