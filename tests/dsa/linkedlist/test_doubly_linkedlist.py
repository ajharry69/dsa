import pytest

from dsa.linkedlist.doubly_linkedlist import Node, LinkedList


class TestNode:
    def test_init(self):
        node = Node(1)

        assert node.value == 1
        assert node.next is None
        assert node.prev is None

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
        assert actual.prev is None
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
        assert actual.prev is None
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
        assert actual.prev is None
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
        "index, value, expected_head, expected_tail, expected_str",
        [
            (0, 0, 0, 5, "<-0-><-1-><-3-><-5->"),
            (1, 2, 1, 5, "<-1-><-2-><-3-><-5->"),
            (2, 4, 1, 5, "<-1-><-3-><-4-><-5->"),
            (3, 6, 1, 6, "<-1-><-3-><-5-><-6->"),
        ],
    )
    def test_set(self, index, value, expected_head, expected_tail, expected_str):
        linked_list = LinkedList(1)
        linked_list.append(3)
        linked_list.append(5)

        actual = linked_list.set(index, value)

        assert actual is True
        assert linked_list.length == 4
        assert str(linked_list) == expected_str
        assert linked_list.head.value == expected_head
        assert linked_list.tail.value == expected_tail

    @pytest.mark.parametrize(
        "index",
        [-1, 5, 100],
    )
    def test_set_out_of_range_index(self, index):
        linked_list = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)

        actual = linked_list.set(index, 9)

        assert actual is False
        assert linked_list.length == 4
        assert str(linked_list) == "<-1-><-2-><-3-><-4->"

    @pytest.mark.parametrize(
        "index, expected_value",
        [
            (0, 1),
            (2, 3),
            (3, 4),
        ],
    )
    def test_get(self, index, expected_value):
        linked_list = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)

        actual = linked_list.get(index)

        assert actual.value == expected_value
        assert str(linked_list) == "<-1-><-2-><-3-><-4->"

    @pytest.mark.parametrize(
        "index",
        [-1, 4, 100],
    )
    def test_get_out_of_range_index(self, index):
        linked_list = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)

        actual = linked_list.get(index)

        assert actual is None

    @pytest.mark.parametrize(
        "index, expected_str, expected_value, expected_head, expected_tail",
        [
            (0, "<-2-><-3-><-4->", 1, 2, 4),
            (2, "<-1-><-2-><-4->", 3, 1, 4),
            (3, "<-1-><-2-><-3->", 4, 1, 3),
        ],
    )
    def test_remove(self, index, expected_str, expected_value, expected_head, expected_tail):
        linked_list = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)

        actual = linked_list.remove(index)

        assert actual.value == expected_value
        assert actual.next is None
        assert actual.prev is None
        assert linked_list.length == 3
        assert str(linked_list) == expected_str
        assert linked_list.head.value == expected_head
        assert linked_list.tail.value == expected_tail

    @pytest.mark.parametrize(
        "index",
        [
            -100,
            -1,
            4,
            100,
        ],
    )
    def test_remove_out_of_range_index(self, index):
        linked_list = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)

        actual = linked_list.remove(index)

        assert actual is None
        assert linked_list.length == 4
        assert str(linked_list) == "<-1-><-2-><-3-><-4->"

    @pytest.mark.parametrize(
        "pop_first, values_to_prepend, expected_head_next, expected_tail_previous, expected_str",
        [
            (True, [], None, None, ""),
            (False, [], None, None, "<-1->"),
            (False, [2], 1, 2, "<-2-><-1->"),
            (False, [2, 3], 2, 2, "<-3-><-2-><-1->"),
            (False, [2, 3, 4, 5], 4, 2, "<-5-><-4-><-3-><-2-><-1->"),
        ],
        ids=[
            "empty",
            "single-item",
            "multiple-items",
            "multiple-items",
            "multiple-items",
        ],
    )
    def test_reverse(
        self,
        pop_first,
        values_to_prepend,
        expected_head_next,
        expected_tail_previous,
        expected_str,
    ):
        linked_list = LinkedList(1)
        if pop_first:
            linked_list.pop_first()
        for value in values_to_prepend:
            linked_list.append(value)

        linked_list.reverse()

        assert str(linked_list) == expected_str
        if linked_list.head:
            assert linked_list.head.prev is None

            if linked_list.head.next:
                assert linked_list.head.next.value == expected_head_next
            else:
                assert linked_list.head.next == expected_head_next

        if linked_list.tail:
            assert linked_list.tail.next is None
            if linked_list.tail.prev:
                assert linked_list.tail.prev.value == expected_tail_previous
            else:
                assert linked_list.tail.prev == expected_tail_previous

    @pytest.mark.parametrize(
        "values_to_prepend, expected_head_next, expected_tail_previous, expected_str",
        [
            ([], None, None, ""),
            ([1], None, None, "<-1->"),
            ([1, 2], 1, 2, "<-2-><-1->"),
            ([1, 2, 3], 2, 2, "<-3-><-2-><-1->"),
            ([1, 2, 3, 4, 5], 2, 4, "<-5-><-2-><-3-><-4-><-1->"),
        ],
        ids=[
            "empty",
            "single-item",
            "multiple-items",
            "multiple-items",
            "multiple-items",
        ],
    )
    def test_swap_first_last(
        self,
        values_to_prepend,
        expected_head_next,
        expected_tail_previous,
        expected_str,
    ):
        linked_list = LinkedList()
        for value in values_to_prepend:
            linked_list.append(value)

        linked_list.swap_first_last()

        assert str(linked_list) == expected_str
        if linked_list.head:
            assert linked_list.head.prev is None

            if linked_list.head.next:
                assert linked_list.head.next.value == expected_head_next
            else:
                assert linked_list.head.next == expected_head_next

        if linked_list.tail:
            assert linked_list.tail.next is None
            if linked_list.tail.prev:
                assert linked_list.tail.prev.value == expected_tail_previous
            else:
                assert linked_list.tail.prev == expected_tail_previous

    @pytest.mark.parametrize(
        "values, expected",
        [
            ([], True),
            ([1], True),
            ([1, 2, 2, 1], True),
            ([1, 2, 3, 4], False),
            ([1, 2, 3, 2, 1], True),
            ([1, 2, 3, 4, 5], False),
        ],
        ids=[
            "empty-list",
            "single-item",
            "even-number-of-items",
            "even-number-of-items",
            "odd-number-of-items",
            "odd-number-of-items",
        ],
    )
    def test_is_palindrome(self, values, expected):
        linked_list = LinkedList()
        for v in values:
            linked_list.append(v)

        actual = linked_list.is_palindrome()

        assert actual is expected

    @pytest.mark.parametrize(
        "values, expected",
        [
            ([], ""),
            ([1], "<-1->"),
            ([1, 2], "<-2-><-1->"),
            ([1, 2, 3, 4], "<-2-><-1-><-4-><-3->"),
            ([1, 2, 3, 4, 5], "<-2-><-1-><-4-><-3-><-5->"),
            ([1, 2, 3, 4, 5, 6], "<-2-><-1-><-4-><-3-><-6-><-5->"),
        ],
    )
    def test_swap_pairs(self, values, expected):
        linked_list = LinkedList()

        for value in values:
            linked_list.append(value=value)

        linked_list.swap_pairs()

        assert str(linked_list) == expected

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
