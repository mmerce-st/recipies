"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """ Test the calc module """

    def test_add(self):
        """ Test adding two numbers """
        self.assertEqual(calc.add(1, 2), 3)

    def test_sub(self):
        """ Test subtracting two numbers """
        self.assertEqual(calc.sub(2, 2), 0)
