"""Testing module liseq"""

from liseq import liseq


def test_special_cases() -> None:
    """A quick test of some special cases."""
    assert liseq([]) == []
    assert liseq('a') == [0]
    assert liseq('abcd') == [0, 1, 2, 3]


def test_your_own_tests() -> None:
    """Add your own tests below."""
    assert False, "Write tests!"  # <- to get your attention
