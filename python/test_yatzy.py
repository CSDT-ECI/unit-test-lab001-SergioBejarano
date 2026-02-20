import pytest
from python.yatzy import Yatzy


class TestSomeBasicCases:

    # caso sencillo
    def test_chance_simple_sum(self):
        assert Yatzy.chance(1, 2, 3, 4, 5) == 15

    def test_yatzy_only_if_five_equal(self):
        assert Yatzy.yatzy([6, 6, 6, 6, 6]) == 50
        assert Yatzy.yatzy([6, 6, 6, 6, 5]) == 0


class TestUpperSection:

    def test_counting_ones_and_twos(self):
        assert Yatzy.ones(1, 1, 2, 3, 4) == 2
        assert Yatzy.twos(2, 2, 5, 6, 1) == 4

    def test_threes_not_present(self):
        assert Yatzy.threes(1, 2, 4, 5, 6) == 0

    def test_some_fours(self):
        game = Yatzy(4, 4, 3, 2, 1)
        assert game.fours() == 8


class TestPairs:

    def test_pair_prefers_highest(self):
        # debería elegir el par de 5 y no el de 3
        assert Yatzy.score_pair(3, 3, 5, 5, 2) == 10

    def test_two_pair_basic(self):
        assert Yatzy.two_pair(1, 1, 2, 2, 6) == 6


class TestKinds:

    def test_three_of_a_kind(self):
        assert Yatzy.three_of_a_kind(4, 4, 4, 2, 1) == 12

    def test_four_of_a_kind_fails_if_only_three(self):
        assert Yatzy.four_of_a_kind(6, 6, 6, 2, 1) == 0


class TestStraightsAndHouse:

    def test_small_straight_order_doesnt_matter(self):
        assert Yatzy.smallStraight(2, 3, 1, 5, 4) == 15

    def test_large_straight(self):
        assert Yatzy.largeStraight(6, 5, 4, 3, 2) == 20

    def test_full_house_example(self):
        assert Yatzy.fullHouse(3, 3, 5, 5, 5) == 21

    def test_not_full_house(self):
        assert Yatzy.fullHouse(2, 2, 2, 2, 3) == 0