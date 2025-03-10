from copy import deepcopy

import pytest

from dsa.sorting import bubble_sort, selection_sort, insertion_sort

__test_cases_sorting = [
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
