import pytest

from dsa.udemy import (
    remove_element,
    find_max_min,
    find_longest_string,
    remove_duplicates,
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
        ([], ''),
        (['apple', 'banana', 'kiwi', 'pear'], "banana"),
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
