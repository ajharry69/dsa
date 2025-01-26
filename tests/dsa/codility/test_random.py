from dsa.codility.random import solution


def test_solution():
    assert solution(images=list(range(1, 7))) == [
        (1, 'I'),
        (2, 'P1'),
        (3, 'P2'),
        (4, 'I'),
        (5, 'P1'),
        (6, 'P2'),
    ]