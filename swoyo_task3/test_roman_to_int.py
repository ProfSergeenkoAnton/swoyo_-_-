from roman_to_int import *
from unittest import TestCase, main

class roman_test(TestCase):
    def test_roman(self):
        #Штатная проверка
        self.assertEqual(roman_to_int("IIIX"),11)
        #Проверка на false
        self.assertEqual(roman_to_int("II"), 3)

