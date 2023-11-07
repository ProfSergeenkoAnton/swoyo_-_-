import unittest
import main
import sys

class main_test(unittest.TestCase):
    def test_prime_numbers(self):
        # Штатная проверка
        self.assertEqual(main.prime_numbers(0, 10),[2,3,5,7])
        # Проверка на false
        self.assertEqual(main.prime_numbers(0, 120), [2, 3, 5, 7])


if __name__ == '__main__':
    unittest.main()