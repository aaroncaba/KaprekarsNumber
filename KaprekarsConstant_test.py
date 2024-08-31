import unittest
from KaprekarsConstant import *


class TestTheThing(unittest.TestCase):
    def test_digits_of_returns_list_of_digits(self):
        self.assertTrue(np.array_equal([1, 3, 2, 4], digits_of(1324, 4)))

    def test_digits_of_reutrns_list_of_length_four(self):
        self.assertEqual(4, len(digits_of(123, 4)))

    def test_digits_of_returns_list_of_zeros_for_zero_input(self):
        self.assertTrue(np.array_equal([0, 0, 0, 0], digits_of(0, 4)))

    def test_digits_of_returns_5_for_5_digit_number(self):
        self.assertTrue(np.array_equal([1, 2, 3, 4, 5], digits_of(12345, 5)))

    def test_digits_to_num_creates_correct_int(self):
        self.assertEqual(1324, digits_to_num([1, 3, 2, 4]))

    def test_digits_bigf(self):
        self.assertTrue(np.array_equal([6, 3, 2, 1], digits_bigf(3216, 4)))

    def test_digits_smallf(self):
        self.assertTrue(np.array_equal([1, 2, 3, 6], digits_smallf(3216, 4)))

    def test_iter_count_is_five_for_1001(self):
        count, final = iter_count(1001, 4)
        self.assertEqual(4, count)

    def test_iter_count_is_1_for_6174(self):
        count, final = iter_count(6174, 4)
        self.assertEqual(0, count)

    def test_iter_count_is_1_for_11111(self):
        count, final = iter_count(11111, 5)
        self.assertEqual(1, count)
