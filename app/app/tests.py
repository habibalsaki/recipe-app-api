from django.test import SimpleTestCase

from app import calc

class TestClasses(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add_numbers(5,6)
        self.assertEqual(res,11)

