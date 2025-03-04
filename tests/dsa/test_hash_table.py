import pytest

from dsa.hash_table import item_in_common


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
