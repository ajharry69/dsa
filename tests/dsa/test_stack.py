import pytest

from dsa.stack import Node, Stack, is_balanced_parentheses


class TestNode:
    def test_init(self):
        node = Node(1)

        assert node.value == 1
        assert node.next is None

    def test_str(self):
        node = Node(1)

        assert str(node) == "1\n"


class TestStack:
    def test_init_when_value_is_none(self):
        stack = Stack(value=None)

        assert stack.size == 0
        assert stack.top is None

    def test_init_when_value_is_not_none(self):
        stack = Stack(value=1)

        assert stack.size == 1
        assert isinstance(stack.top, Node)
        assert stack.top.value == 1

    @pytest.mark.parametrize(
        "values, expected",
        [
            ([], "1\n"),
            ([2], "2\n1\n"),
            ([2, 3], "3\n2\n1\n"),
        ],
    )
    def test_str(self, values, expected):
        stack = Stack(1)
        for value in values:
            stack.push(value)

        actual = str(stack)

        assert actual == expected

    @pytest.mark.parametrize(
        "head, values, expected_size, expected_top",
        [
            (None, [10], 1, 10),
            (1, [20], 2, 20),
            (1, [2, 30], 3, 30),
        ],
    )
    def test_push(self, head, values, expected_size, expected_top):
        stack = Stack(head)

        actual = [stack.push(value=value) for value in values]

        assert all(actual)
        assert stack.size == expected_size
        assert stack.top.value == expected_top

    @pytest.mark.parametrize(
        "values, expected",
        [
            ([], None),
            ([1], 1),
        ],
    )
    def test_pop_and_empty_stack(self, values, expected):
        stack = Stack(value=None)
        for value in values:
            stack.push(value=value)

        actual = stack.pop()

        if expected is None:
            assert actual is None
        else:
            assert actual.next is None
            assert actual.value == expected
        assert stack.size == 0
        assert stack.top is None

    @pytest.mark.parametrize(
        "head, values, expected_size, expected_top, expected_value",
        [
            (1, [2], 1, 1, 2),
            (1, [2, 3], 2, 2, 3),
        ],
    )
    def test_pop(self, head, values, expected_size, expected_top, expected_value):
        stack = Stack(value=head)
        for value in values:
            stack.push(value=value)

        actual = stack.pop()

        assert actual.value == expected_value
        assert actual.next is None
        assert stack.size == expected_size
        assert stack.top.value == expected_top

    @pytest.mark.parametrize(
        "values, expected",
        [
            ([], True),
            ([1], False),
            ([1, 2, 3], False),
        ],
    )
    def test_is_empty(self, values, expected):
        stack = Stack()
        for value in values:
            stack.push(value=value)

        actual = stack.is_empty()

        assert actual == expected

    @pytest.mark.parametrize(
        "values, expected",
        [
            ([], None),
            ([1], '1\n'),
            ([1, 2, 3], '3\n'),
        ],
    )
    def test_peek(self, values, expected):
        stack = Stack()
        for value in values:
            stack.push(value=value)

        actual = stack.peek()

        if expected is None:
            assert actual == expected
        else:
            assert str(actual) == expected


@pytest.mark.parametrize(
    "data, expected",
    [
        ("", True),
        ("(", False),
        (")", False),
        ("((", False),
        ("))", False),
        ("()", True),
        (")())", False),
        ("()())", False),
        ("(()())", True),
        ("((()))", True),
        ("(()))", False),
        ("(()())", True),
        ("(()", False),
        ("())", False),
        (")(", False),
        ("()()()()", True),
        ("(())(())", True),
        ("(()()())", True),
        ("(()()(example))", True),
        ("((())", False),
    ],
)
def test_is_balanced_parentheses(data, expected):
    actual = is_balanced_parentheses(data=data)

    assert actual is expected
