__author__ = 'Gabi'

import unittest

from exercise import DigitPowers


class TestDigitPowers(unittest.TestCase):

    def test_digit_powers_exist(self):
        dp_result = DigitPowers()

    def test_digit_powers_has_sum_numbers(self):
        dp_result = DigitPowers()
        assert dp_result.sum_numbers is not None, "dfp_result sum_numbers is None"

    def test_digit_powers_sum_of_powers(self):
        dp_result = DigitPowers()
        assert dp_result.sum_of_powers(1634, 4) == 1634, "dfp_result is not correct"

if __name__ == "__main__":
    unittest.main()
