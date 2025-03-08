import pytest

from dsa.hash_table import (
    item_in_common,
    find_duplicates,
    find_duplicates_2,
    first_non_repeating_char,
    group_anagrams,
    two_sum,
    subarray_sum,
    has_unique_chars,
    has_unique_chars_1,
)


@pytest.mark.parametrize(
    "list1, list2, expected",
    [
        ([], [], False),
        ([1, 3, 5], [], False),
        ([], [1, 3, 5], False),
        ([1, 3, 5], [2, 4, 5], True),
        ([1, 3, 5], [2, 4, 6], False),
        ([1, 3, 5], [2, 4, 6, 7], False),
        ([2, 4, 6, 7], [1, 3, 5], False),
        ([2, 4, 6, 5], [1, 3, 5], True),
    ],
)
def test_item_in_common(list1, list2, expected):
    actual = item_in_common(list1=list1, list2=list2)

    assert actual is expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([], []),
        ([1, 2, 3, 4, 5], []),
        ([1, 1, 2, 2, 3], [1, 2]),
        ([1, 1, 1, 1, 1], [1]),
        ([1, 2, 3, 3, 3, 4, 4, 5], [3, 4]),
        ([1, 1, 2, 2, 2, 3, 3, 3, 3], [1, 2, 3]),
        ([1, 1, 1, 2, 2, 2, 3, 3, 3, 3], [1, 2, 3]),
    ],
)
def test_find_duplicates(nums, expected):
    actual = find_duplicates(nums=nums)
    actual_2 = find_duplicates_2(nums=nums)

    assert actual == actual_2 == expected


@pytest.mark.parametrize(
    "string, expected",
    [
        ("leetcode", "l"),
        ("hello", "h"),
        ("aabbcc", None),
    ],
)
def test_first_non_repeating_char(string, expected):
    actual = first_non_repeating_char(string)

    assert actual == expected


@pytest.mark.parametrize(
    "strings, expected",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        (
            ["abc", "cba", "bac", "foo", "bar"],
            [["abc", "cba", "bac"], ["foo"], ["bar"]],
        ),
        (
            ["listen", "silent", "triangle", "integral", "garden", "ranged"],
            [["listen", "silent"], ["triangle", "integral"], ["garden", "ranged"]],
        ),
    ],
)
def test_group_anagrams(strings, expected):
    actual = group_anagrams(strings=strings)

    assert actual == expected


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([5, 1, 7, 2, 9, 3], 10, [1, 4]),
        ([4, 2, 11, 7, 6, 3], 9, [1, 3]),
        ([1, 2, 3, 4, 5], 10, []),
        ([1, 2, 3, 4, 5], 3, [0, 1]),
        ([], 0, []),
        ([10, 15, 5, 2, 8, 1, 7], 12, [0, 3]),
        ([1, 3, 5, 7, 9], 10, [1, 3]),
        ([1, 2, 3, 4, 5], 7, [2, 3]),
    ],
)
def test_two_sum(nums, target, expected):
    actual = two_sum(nums=nums, target=target)

    assert actual == expected


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([1, 2, 3, 4, 5], 9, [1, 3]),
        ([-1, 2, 3, -4, 5], 0, [0, 3]),
        ([2, 3, 4, 5, 6], 3, [1, 1]),
        ([], 0, []),
    ],
)
def test_subarray_sum(nums, target, expected):
    actual = subarray_sum(nums=nums, target=target)

    assert actual == expected


__test_cases_has_unique_chars = [
    ("abcdefg", True),
    ("hello", False),
    ("", True),
    ("0123456789", True),
    ("abacadaeaf", False),
]


@pytest.mark.parametrize(
    "string, expected",
    __test_cases_has_unique_chars,
)
def test_has_unique_chars(string, expected):
    actual = has_unique_chars(string=string)

    assert actual is expected


@pytest.mark.parametrize(
    "string, expected",
    __test_cases_has_unique_chars,
)
def test_has_unique_chars_1(string, expected):
    actual = has_unique_chars_1(string=string)

    assert actual is expected
