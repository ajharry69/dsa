from copy import deepcopy

import pytest

from dsa.udemy import (
    remove_element,
    find_max_min,
    find_longest_string,
    remove_duplicates,
    max_profit,
    rotate,
    rotate_1,
    max_subarray,
    max_subarray_1,
    max_subarray_2,
)


@pytest.mark.parametrize(
    "nums, val, expected, expected_nums",
    [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 1, 7, [-2, -3, 4, -1, 2, -5, 4]),
        ([1, 2, 3, 4, 5, 6], 6, 5, [1, 2, 3, 4, 5]),
        ([-1, -2, -3, -4, -5], -1, 4, [-2, -3, -4, -5]),
        ([], 1, 0, []),
        ([1, 1, 1, 1, 1], 1, 0, []),
    ],
)
def test_remove_element(nums, val, expected, expected_nums):
    actual = remove_element(nums=nums, val=val)

    assert actual == expected
    assert nums == expected_nums


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([5, 3, 8, 1, 6, 9], (9, 1)),
    ],
)
def test_find_max_min(nums, expected):
    actual = find_max_min(nums=nums)

    assert actual == expected


@pytest.mark.parametrize(
    "strings, expected",
    [
        ([], ""),
        (["apple", "banana", "kiwi", "pear"], "banana"),
    ],
)
def test_find_longest_string(strings, expected):
    actual = find_longest_string(strings=strings)

    assert actual == expected


@pytest.mark.parametrize(
    "nums, expected_length, expected_no_duplicate_nums, expected_nums",
    [
        ([], 0, [], []),
        ([1, 1, 1, 1, 1], 1, [1], [1, 1, 1, 1, 1]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([1, 1, 2, 2, 3, 4, 5, 5], 5, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 4, 5, 5]),
    ],
)
def test_remove_duplicates(nums, expected_length, expected_no_duplicate_nums, expected_nums):
    actual = remove_duplicates(nums=nums)

    assert expected_length == actual
    assert nums[:expected_length] == expected_no_duplicate_nums
    assert nums == expected_nums


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([], 0),
        ([7, 1, 5, 3, 6, 4], 5),
        ([1, 2, 3, 4, 5, 6], 5),
        ([7, 6, 4, 3, 1], 0),
    ],
    ids=[
        "no prices",
        "mixed prices",
        "ascending prices",
        "descending prices",
    ],
)
def test_max_profit(prices, expected):
    actual = max_profit(prices=prices)

    assert actual == expected


__test_cases_rotate = [
    ([], 1, []),
    ([1], 1, [1]),
    ([1], 2, [1]),
    ([1, 2], 0, [1, 2]),
    ([1, 2], 1, [2, 1]),
    ([1, 2], 2, [1, 2]),
    ([1, 2, 3, 4, 5], 6, [5, 1, 2, 3, 4]),
    ([1, 2, 3, 4, 5], 21, [5, 1, 2, 3, 4]),
    ([1, 2, 3, 4, 5], 50, [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
]


@pytest.mark.parametrize(
    "nums, k, expected",
    deepcopy(__test_cases_rotate),
)
def test_rotate(nums, k, expected):
    actual = rotate(nums=nums, k=k)

    assert actual is None
    assert nums == expected


@pytest.mark.parametrize(
    "nums, k, expected",
    deepcopy(__test_cases_rotate),
)
def test_rotate_1(nums, k, expected):
    actual = rotate_1(nums=nums, k=k)

    assert actual is None
    assert nums == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([], (0, [])),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], (6, [4, -1, 2, 1])),
        ([1, 2, 3, -4, 5, 6], (13, [1, 2, 3, -4, 5, 6])),
        ([-1, -2, -3, -4, -5], (-1, [-1])),
    ],
)
def test_max_subarray(nums, expected):
    actual = max_subarray(nums=nums)

    assert actual == expected


__test_cases_max_subarray = [
    ([], 0),
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1, 2, 3, -4, 5, 6], 13),
    ([-1, -2, -3, -4, -5], -1),
]


@pytest.mark.parametrize(
    "nums, expected",
    __test_cases_max_subarray,
)
def test_max_subarray_1(nums, expected):
    actual = max_subarray_1(nums=nums)

    assert actual == expected


@pytest.mark.parametrize(
    "nums, expected",
    __test_cases_max_subarray,
)
def test_max_subarray_2(nums, expected):
    actual = max_subarray_2(nums=nums)

    assert actual == expected
