# Lab 5 -> Antonio Ruiz Benito

import unittest

from calculator import add
from calculator import subtract
from calculator import multiply
from calculator import divide

class Test_Calculator(unittest.TestCase):

    def test_add(self):
        """Test para la funcion sumar"""
        self.assertEqual(add(10, 29), 39)

        self.assertEqual(add(-3, 9), 6)

        self.assertEqual(add(-5, -10), -15)

    
    def test_subtract(self):
        """Test para la funcion restar"""
        self.assertEqual(subtract(1987, 29), 1958)

        self.assertEqual(subtract(-9, 2), -11)

        self.assertEqual(subtract(-10, -33), 23)

    def test_multiply(self):
        """Test para la funcion multiplicar"""
        self.assertEqual(multiply(3, 1000), 3000)

        self.assertEqual(multiply(-7, 9), -63)

        self.assertEqual(multiply(-2, -5), 10)

    def test_divide(self):
        """
        Test para la funcion division, controlando la excepcion 
        que pudiese ocurrir al dividir entre 0 
        """
        self.assertEqual(divide(10, 5), 2)

        self.assertEqual(divide(10, 100), 0.1)


if __name__ == '__main__':
    unittest.main()
