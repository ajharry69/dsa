import pytest

from dsa.codility.proxify import solution


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([2, 4, 1, 5, 7], 10),
    ],
)
def test_solution(prices, expected):
    actual = solution(prices=prices)

    assert actual == expected
