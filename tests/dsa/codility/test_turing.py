import pytest

from dsa.codility.turing import find_three_sum_1, find_three_sum_2


@pytest.mark.parametrize(
    "values, expected",
    [
        ([], []),
        ([0], []),
        ([1], []),
        ([1, 2], []),
        ([1, 2, 3], []),
        ([1, 2, -3], [1, 2, -3]),
        ([1, 2, 3, -3], [1, 2, -3]),
        ([1, 3, 0, -3], [3, 0, -3]),
    ],
)
def test_find_three_sum_1(values, expected):
    actual = find_three_sum_1(values)

    assert actual == expected


@pytest.mark.parametrize(
    "values, expected",
    [
        ([], []),
        ([0], []),
        ([1], []),
        ([1, 2], []),
        ([1, 2, 3], []),
        ([1, 2, -3], [[1, 2, -3]]),
        ([1, 2, 3, -3], [[1, 2, -3]]),
        ([1, 3, 0, -3], [[3, 0, -3]]),
    ],
)
def test_find_three_sum_2(values, expected):
    actual = find_three_sum_2(values)

    assert actual == expected
