import pytest
from python.yatzy import Yatzy

class TestCrazyChance:

    def test_all_even(self):
        assert Yatzy.crazy_chance(2, 4, 6, 2, 2) == 48

    def test_all_odd(self):
        assert Yatzy.crazy_chance(1, 1, 3, 5, 5) == 30

    def test_mixed_even_and_odd(self):
        assert Yatzy.crazy_chance(2, 4, 3, 5, 6) == 52