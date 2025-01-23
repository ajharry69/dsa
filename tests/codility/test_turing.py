import pytest

from codility.turing import solution


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
def test_solution(values, expected):
    actual = solution(values)

    assert actual == expected
