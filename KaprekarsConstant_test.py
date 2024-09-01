import unittest
from KaprekarsConstant import *


class TestTheThing(unittest.TestCase):

    def test_digits_of_returns_list_of_sorted_digits(self):
        kc = KaprekaersConstant(4)
        self.assertTrue(np.array_equal(
            [1, 2, 3, 4], kc.digits_of(1324,  type='small')))

    def test_digits_of_returns_list_of_reverse_sorted_digits(self):
        kc = KaprekaersConstant(4)
        self.assertTrue(np.array_equal(
            [4, 3, 2, 1], kc.digits_of(1324,  type='big')))

    def test_digits_of_reutrns_list_of_length_four(self):
        kc = KaprekaersConstant(4)
        self.assertEqual(4, len(kc.digits_of(123,  type='small')))

    def test_digits_of_returns_list_of_zeros_for_zero_input(self):
        kc = KaprekaersConstant(4)
        self.assertTrue(np.array_equal(
            [0, 0, 0, 0], kc.digits_of(0,  type='small')))

    def test_digits_of_returns_5_for_5_digit_number(self):
        kc = KaprekaersConstant(5)
        self.assertTrue(np.array_equal(
            [1, 2, 3, 4, 5], kc.digits_of(12345, type='small')))

    def test_digits_to_num_creates_correct_int(self):
        kc = KaprekaersConstant(4)
        self.assertEqual(1324, kc.digits_to_num([1, 3, 2, 4]))

    def test_iter_count_is_five_for_1001(self):
        kc = KaprekaersConstant(4)
        count, final = kc.iter_count(1001)
        self.assertEqual(4, count)

    def test_iter_count_is_1_for_6174(self):
        kc = KaprekaersConstant(4)
        count, final = kc.iter_count(6174)
        self.assertEqual(0, count)

    def test_iter_count_is_1_for_11111(self):
        kc = KaprekaersConstant(5)
        count, final = kc.iter_count(11111)
        self.assertEqual(1, count)
