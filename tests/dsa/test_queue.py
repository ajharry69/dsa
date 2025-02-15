import pytest

from dsa.queue import Node, Queue, QueueUsingStack


class TestNode:
    def test_init(self):
        node = Node(1)

        assert node.value == 1
        assert node.next is None

    def test_str(self):
        node = Node(1)

        assert str(node) == "<-1"


class TestQueue:
    def test_init_when_value_is_none(self):
        queue = Queue(value=None)

        assert queue.size == 0
        assert queue.front is None
        assert queue.back is None

    def test_init_when_value_is_not_none(self):
        queue = Queue(value=1)

        assert queue.size == 1
        assert isinstance(queue.front, Node)
        assert queue.front.value == 1
        assert isinstance(queue.back, Node)
        assert queue.back.value == 1

    @pytest.mark.parametrize(
        "values, expected",
        [
            ([], "<-1"),
            ([2], "<-1<-2"),
            ([2, 3], "<-1<-2<-3"),
        ],
    )
    def test_str(self, values, expected):
        queue = Queue(1)
        for value in values:
            queue.enqueue(value)

        actual = str(queue)

        assert actual == expected

    @pytest.mark.parametrize(
        "head, values, expected_size, expected_front, expected_back",
        [
            (None, [1], 1, 1, 1),
            (1, [2], 2, 1, 2),
            (1, [2, 3], 3, 1, 3),
        ],
    )
    def test_enqueue(self, head, values, expected_size, expected_front, expected_back):
        queue = Queue(head)

        actual = [queue.enqueue(value=value) for value in values]

        assert all(actual)
        assert queue.size == expected_size
        assert queue.front.value == expected_front
        assert queue.back.value == expected_back

    @pytest.mark.parametrize(
        "values, expected",
        [
            ([], None),
            ([1], 1),
        ],
    )
    def test_dequeue_and_empty_queue(self, values, expected):
        queue = Queue(value=None)
        for value in values:
            queue.enqueue(value=value)

        actual = queue.dequeue()

        if expected is None:
            assert actual is None
        else:
            assert actual.next is None
            assert actual.value == expected
        assert queue.size == 0
        assert queue.front is None
        assert queue.back is None

    @pytest.mark.parametrize(
        "head, values, expected_size, expected_front, expected_back",
        [
            (1, [2], 1, 2, 2),
            (1, [2, 3], 2, 2, 3),
        ],
    )
    def test_dequeue(self, head, values, expected_size, expected_front, expected_back):
        queue = Queue(head)
        for value in values:
            queue.enqueue(value=value)

        actual = queue.dequeue()

        assert actual.value == 1
        assert actual.next is None
        assert queue.size == expected_size
        assert queue.front.value == expected_front
        assert queue.back.value == expected_back


class TestQueueUsingStack:
    @pytest.mark.parametrize(
        "values, expected_peak",
        [
            ([1, 2, 3], 1),
        ],
    )
    def test_enqueue(self, values, expected_peak):
        queue = QueueUsingStack()

        for value in values:
            queue.enqueue(value=value)

        assert queue.peek() == expected_peak
        assert queue.is_empty() is False

    @pytest.mark.parametrize(
        "values, expected, expected_peak",
        [
            ([1, 2, 3], 1, 2),
        ],
    )
    def test_dequeue(self, values, expected, expected_peak):
        queue = QueueUsingStack()

        for value in values:
            queue.enqueue(value=value)

        actual = queue.dequeue()

        assert actual == expected
        assert queue.peek() == expected_peak
        assert queue.is_empty() is False
