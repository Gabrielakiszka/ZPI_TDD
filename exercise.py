__author__ = 'Gabi'


class DigitPowers():
    def __init__(self):
        self.sum_numbers = 0

    @staticmethod
    def sum_of_powers(number, power):
        digits = [int(d) for d in str(number)]
        return sum(d**power for d in digits)


