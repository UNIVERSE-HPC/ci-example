import unittest
from mymath.factorial import factorial


class TestFactorialFunctions(unittest.TestCase):

  def test_3(self):
    self.assertEqual(factorial(3), 6)

  def test_5(self):
    self.assertEqual(factorial(5), 120)

  def test_negative(self):
    with self.assertRaises(ValueError):
      factorial(-1)
