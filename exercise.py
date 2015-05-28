__author__ = 'Gabi'


class DigitPowers():
    def __init__(self):
        self.sum_numbers = 0

    @staticmethod
    def sum_of_powers(number, power):
        digits = [int(d) for d in str(number)]
        return sum(d**power for d in digits)

    def calc_max_value(self, power):

        start = 9
        while self.sum_of_powers(start, power) > start:
            start = start * 10 + 9
        return self.sum_of_powers(start, power)

    def solution(self, power):
        for number in range(10, self.calc_max_value(power)+1):
            if self.sum_of_powers(number, power) == number:
                self.sum_numbers += number
        return self.sum_numbers






