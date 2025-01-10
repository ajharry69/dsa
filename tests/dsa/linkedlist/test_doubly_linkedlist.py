import pytest

from dsa.linkedlist.doubly_linkedlist import Node, LinkedList


class TestNode:
    def test_init(self):
        node = Node(1)

        assert node.value == 1
        assert node.next is None
        assert node.previous is None

    def test_str(self):
        node = Node(1)

        assert str(node) == "<-1->"


class TestLinkedList:
    def test_init(self):
        linked_list = LinkedList(1)

        assert linked_list.length == 1

        assert isinstance(linked_list.head, Node)
        assert linked_list.head.value == 1

        assert isinstance(linked_list.tail, Node)
        assert linked_list.tail.value == 1

    def test_pop_first(self):
        linked_list = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)

        actual = linked_list.pop_first()

        assert actual.value == 1
        assert actual.next is None
        assert actual.previous is None
        assert linked_list.length == 3
        assert str(linked_list) == "<-2-><-3-><-4->"
        assert linked_list.head.value == 2
        assert linked_list.tail.value == 4

    def test_pop_first_when_list_has_no_items(self):
        linked_list = LinkedList(1)
        linked_list.pop_first()  # clear the list

        actual = linked_list.pop_first()

        assert actual is None
        assert linked_list.length == 0
        assert str(linked_list) == ""
        assert linked_list.head is None
        assert linked_list.tail is None

    def test_pop_first_when_list_has_one_item(self):
        linked_list = LinkedList(1)

        actual = linked_list.pop_first()

        assert actual.value == 1
        assert linked_list.length == 0
        assert str(linked_list) == ""
        assert linked_list.head is None
        assert linked_list.tail is None

    @pytest.mark.parametrize(
        "pop_first, values_to_append, expected_str, expected_length",
        [
            (True, [2], "<-2->", 1),
            (False, [2], "<-1-><-2->", 2),
            (True, [2, 3], "<-2-><-3->", 2),
            (False, [2, 3], "<-1-><-2-><-3->", 3),
        ],
    )
    def test_append(self, pop_first, values_to_append, expected_str, expected_length):
        linked_list = LinkedList(1)
        if pop_first:
            linked_list.pop_first()

        for value in values_to_append:
            assert linked_list.append(value) is True

        assert linked_list.length == expected_length
        assert str(linked_list) == expected_str

    def test_pop(self):
        linked_list = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)

        actual = linked_list.pop()

        assert actual.value == 4
        assert actual.next is None
        assert actual.previous is None
        assert linked_list.length == 3
        assert str(linked_list) == "<-1-><-2-><-3->"

    def test_pop_when_list_has_no_items(self):
        linked_list = LinkedList(1)
        linked_list.pop_first()  # clear the list

        actual = linked_list.pop()

        assert actual is None
        assert linked_list.length == 0
        assert str(linked_list) == ""
        assert linked_list.head is None
        assert linked_list.tail is None

    def test_pop_when_list_has_one_item(self):
        linked_list = LinkedList(1)

        actual = linked_list.pop()

        assert actual.value == 1
        assert actual.next is None
        assert actual.previous is None
        assert linked_list.length == 0
        assert str(linked_list) == ""
        assert linked_list.head is None
        assert linked_list.tail is None

    @pytest.mark.parametrize(
        "pop_first, values_to_prepend, expected_str, expected_length",
        [
            (True, [2], "<-2->", 1),
            (False, [2], "<-2-><-1->", 2),
            (True, [2, 3], "<-3-><-2->", 2),
            (False, [2, 3], "<-3-><-2-><-1->", 3),
        ],
    )
    def test_prepend(self, pop_first, values_to_prepend, expected_str, expected_length):
        linked_list = LinkedList(1)
        if pop_first:
            linked_list.pop_first()

        for value in values_to_prepend:
            assert linked_list.prepend(value) is True

        assert linked_list.length == expected_length
        assert str(linked_list) == expected_str

    @pytest.mark.parametrize(
        "values, expected",
        [
            ([], "<-1->"),
            ([2], "<-1-><-2->"),
            ([2, 3], "<-1-><-2-><-3->"),
        ],
    )
    def test_str(self, values, expected):
        linked_list = LinkedList(1)

        for value in values:
            linked_list.append(value)

        assert str(linked_list) == expected