from unittest import TestCase
from Lottery import Lottery


class TestLottery(TestCase):
    def test_rand_numbers(self):
        my_lotto = Lottery()
        self.assertTrue(len(my_lotto.rand_numbers()) == 6)

    def test_rand_numbers(self):
        my_lotto = Lottery()
        self.assertFalse(len(my_lotto.rand_numbers()) != 6)

    def test_valid_numbers(self):
        my_lotto = Lottery()
        self.false

    def test_valid_range(self):
        self.fail()
