from copy import deepcopy

import pytest

from dsa.sorting import bubble_sort, selection_sort, insertion_sort, merge, merge_sort

__test_cases_sorting = [
    ([], []),
    ([1], [1]),
    ([3, 1, 4, 2], [1, 2, 3, 4]),
    ([4, 2, 6, 5, 1, 3], [1, 2, 3, 4, 5, 6]),
    ([4, 2, 6, 5, 3, 1], [1, 2, 3, 4, 5, 6]),
]


@pytest.mark.parametrize(
    "my_list, expected",
    deepcopy(__test_cases_sorting),
)
def test_bubble_sort(my_list, expected):
    actual = bubble_sort(my_list=my_list)

    assert actual is None
    assert my_list == expected


@pytest.mark.parametrize(
    "my_list, expected",
    deepcopy(__test_cases_sorting),
)
def test_selection_sort(my_list, expected):
    actual = selection_sort(my_list=my_list)

    assert actual is None
    assert my_list == expected


@pytest.mark.parametrize(
    "my_list, expected",
    deepcopy(__test_cases_sorting),
)
def test_insertion_sort(my_list, expected):
    actual = insertion_sort(my_list=my_list)

    assert actual is None
    assert my_list == expected


@pytest.mark.parametrize(
    "l1, l2, expected",
    [
        ([], [], []),
        ([1], [], [1]),
        ([], [1], [1]),
        ([1], [1], [1, 1]),
        ([1, 3, 7, 8], [2, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7, 8]),
        ([1, 3, 7, 8], [2, 4, 5, 6, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([1, 3, 7, 8, 9], [2, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([1, 3, 7, 8, 9], [2, 4, 5, 6, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]),
    ],
)
def test_merge(l1, l2, expected):
    actual = merge(l1=l1, l2=l2)

    assert actual == expected


@pytest.mark.parametrize(
    "my_list, expected",
    deepcopy(__test_cases_sorting),
)
def test_merge_sort(my_list, expected):
    actual = merge_sort(my_list=my_list)

    assert actual == expected
