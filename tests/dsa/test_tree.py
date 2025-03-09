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

    @pytest.mark.parametrize(
        "values, expected",
        [
            ([], []),
            ([47], [47]),
            ([47, 21], [47, 21]),
            ([47, 21, 76, 18, 27, 52, 82], [47, 21, 18, 27, 76, 52, 82]),
        ],
    )
    def test_dfs_pre_order(self, values, expected):
        tree = BinarySearchTree()
        for value in values:
            tree.insert(value=value)

        actual = tree.dfs_pre_order()

        assert actual == expected

    @pytest.mark.parametrize(
        "values, expected",
        [
            ([], []),
            ([47], [47]),
            ([47, 21], [21, 47]),
            ([47, 21, 76, 18, 27, 52, 82], [18, 27, 21, 52, 82, 76, 47]),
        ],
    )
    def test_dfs_post_order(self, values, expected):
        tree = BinarySearchTree()
        for value in values:
            tree.insert(value=value)

        actual = tree.dfs_post_order()

        assert actual == expected

    @pytest.mark.parametrize(
        "values, expected",
        [
            ([], []),
            ([47], [47]),
            ([47, 21], [21, 47]),
            ([47, 21, 76, 18, 27, 52, 82], [18, 21, 27, 47, 52, 76, 82]),
        ],
    )
    def test_dfs_in_order(self, values, expected):
        tree = BinarySearchTree()
        for value in values:
            tree.insert(value=value)

        actual = tree.dfs_in_order()

        assert actual == expected
