import pytest

from dsa.heap import find_kth_smallest, stream_max, reposition_zeros


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([3, 2, 1, 5, 6, 4], 2, 2),
        ([6, 5, 4, 3, 2, 1], 3, 3),
        ([1, 2, 3, 4, 5, 6], 4, 4),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 7, 5),
    ],
)
def test_find_kth_smallest(nums, k, expected):
    actual = find_kth_smallest(nums=nums, k=k)

    assert actual == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([1, 2, 2, 1, 3, 3, 3, 2, 2], [1, 2, 2, 2, 3, 3, 3, 3, 3]),
        ([-1, -2, -3, -4, -5], [-1, -1, -1, -1, -1])
    ],
)
def test_stream_max(nums, expected):
    actual = stream_max(nums=nums)

    assert actual == expected


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
