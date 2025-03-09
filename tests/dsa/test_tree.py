import pytest

from dsa.tree import BinarySearchTree


class TestBinarySearchTree:
    @pytest.mark.parametrize(
        "values, expected",
        [
            ([], []),
            ([47], [47]),
            ([47, 21], [47, 21]),
            ([47, 21, 76, 18, 27, 52, 82], [47, 21, 76, 18, 27, 52, 82]),
        ],
    )
    def test_bfs(self, values, expected):
        tree = BinarySearchTree()
        for value in values:
            tree.insert(value=value)

        actual = tree.bfs()

        assert actual == expected
