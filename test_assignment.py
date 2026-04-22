import pytest
import inspect
from assignment import sum_array, sum_positive, more_odds, find_max, count_target


def uses_loop(func):
    source = inspect.getsource(func)
    return "for" in source or "while" in source


# Exercise 1
@pytest.mark.parametrize("lst, expected", [
    ([12, 13, 14, 15], 54),
    ([1, 2, 3], 6),
    ([0, 0, 0], 0),
])
def test_sum_array(lst, expected):
    assert sum_array(lst) == expected
    assert uses_loop(sum_array)


# Exercise 2
@pytest.mark.parametrize("lst, expected", [
    ([5, -3, 4, -10], 9),
    ([-1, -2, -3], 0),
    ([1, 2, 3], 6),
])
def test_sum_positive(lst, expected):
    assert sum_positive(lst) == expected
    assert uses_loop(sum_positive)


# Exercise 3
@pytest.mark.parametrize("lst, expected", [
    ([2, 3, 4, 1, 7], "YES"),
    ([2, 4, 6], "NO"),
    ([1, 3, 5], "YES"),
])
def test_more_odds(lst, expected):
    assert more_odds(lst) == expected
    assert uses_loop(more_odds)


# Exercise 4
@pytest.mark.parametrize("lst, expected", [
    ([3, -2, 4, 7, -6], 7),
    ([1], 1),
    ([-5, -2, -10], -2),
])
def test_find_max(lst, expected):
    assert find_max(lst) == expected
    assert uses_loop(find_max)


# Exercise 5
@pytest.mark.parametrize("lst, target, expected", [
    ([1, 5, 4, 5, 3, 9], 5, 2),
    ([1, 2, 3], 4, 0),
    ([7, 7, 7], 7, 3),
])
def test_count_target(lst, target, expected):
    assert count_target(lst, target) == expected
    assert uses_loop(count_target)
