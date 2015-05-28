__author__ = 'Gabi'

# Exercise 15
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
#     1634 = 14 + 64 + 34 + 44
#     8208 = 84 + 24 + 04 + 84
#     9474 = 94 + 44 + 74 + 44
#
# As 1 = 14 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


class DigitPowers():
    def __init__(self):
        self.sum_numbers = 0

    # Static method: Sum of powers: addition of definite powers of digits of a given number.

    # number - The number to be check out, if can be written as the sum of definite powers of its digits.
    # power - The number to that digits of number are escalated.

    # Examples
    # multiplex(42, 2)
    #  # => 20
    #
    # multiplex(25, 3)
    #  # => 133
    #
    # Returns the sum of definite powers of digits of the number.

    @staticmethod
    def sum_of_powers(number, power):
        digits = [int(d) for d in str(number)]
        return sum(d**power for d in digits)

    # Calc max value: it calculates a maximum number that can be written
    # as the sum of definite powers of its digits if all are an equal 9
    # (digits for the sum must have the same number of digits as a candidate).
    #
    # It is calculated by the sum of powers.
    #
    # start - The maximum number for definite order of magnitude, formula: start = start * 10 + 9.
    # power - The number to that digits of the given number are escalated.
    #
    # Examples
    # multiplex(2)
    #  # => 243
    #
    # multiplex(3)
    #  # => 2916
    # Returns the maximum number that can be written as the sum of definite powers
    # of its digits if all are an equal 9.

    def calc_max_value(self, power):

        start = 9
        while self.sum_of_powers(start, power) > start:
            start = start * 10 + 9
        return self.sum_of_powers(start, power)

    # Solution: addition of all the numbers that can be written as the sum of definite powers of their digits.
    #
    # Search range starts from at least 10, because cannot form a sum of digits if numbers < 10.
    # Search range ends up the maximum number that is calculated by the calc max value (increased by 1), because
    # digits for the sum must have the same number of digits as a candidate.
    #
    # It checks out, if the given number is an equal the sum of definite powers of digits of the number.
    # If it's true, this number is added to the sum numbers.
    #
    # Returns the sum of all the numbers that can be written as the sum of definite powers of their digits.

    def solution(self, power):
        for number in range(10, self.calc_max_value(power)+1):
            if self.sum_of_powers(number, power) == number:
                self.sum_numbers += number
        return self.sum_numbers

dp_results = DigitPowers()
print(dp_results.solution(5))





