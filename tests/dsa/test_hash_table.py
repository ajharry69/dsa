import pytest

from dsa.hash_table import (
    item_in_common,
    find_duplicates,
    find_duplicates_2,
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
