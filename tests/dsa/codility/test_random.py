import pytest

from dsa.codility.random import solution, reposition_zeros, move_zeros, get_triangle_type


def test_solution():
    assert solution(images=list(range(1, 7))) == [
        (1, 'I'),
        (2, 'P1'),
        (3, 'P2'),
        (4, 'I'),
        (5, 'P1'),
        (6, 'P2'),
    ]


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 3, 0, 12, 0], [3, 12, 0, 0, 0]),
        ([-1, 0, 3, 0, 0, 12, 0], [-1, 3, 12, 0, 0, 0, 0]),
    ],
)
def test_reposition_zeros(nums, expected):
    actual = reposition_zeros(nums=nums)

    assert actual == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 3, 0, 12, 0], [3, 12, 0, 0, 0]),
        ([-1, 0, 3, 0, 0, 12, 0], [-1, 3, 12, 0, 0, 0, 0]),
    ],
)
def test_move_zeros(nums, expected):
    actual = move_zeros(nums=nums)

    assert actual == expected


@pytest.mark.parametrize(
    "length1, length2, length3, expected",
    [
        (0, 0, 0, "Impossible"),
        (0, -1, 0, "Impossible"),
        (1, 2, 3, "Scalene"),
        (1, 2, 2, "Isosceles"),
        (2, 2, 2, "Equilateral"),
    ],
)
def test_get_triangle_type(length1, length2, length3, expected):
    actual = get_triangle_type(length1, length2, length3)

    assert actual == expected
