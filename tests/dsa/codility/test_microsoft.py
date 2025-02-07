import pytest

from dsa.codility.microsoft import solution1, solution2, solution3, reverse_polish_notation


def test_solution1():
    assert solution1([1, 1, 4, 4], 4, 2) == True
    assert solution1([1, 1, 2, 4], 4, 1) == False
    assert solution1([4, 2, 5], 5, 2) == True
    assert solution1([4, 2, 2, 2, 5], 5, 2) == False


def test_solution2():
    """
    m = 5
    l = 6
    r = 10
    ---------
    m = 8
    l = 6
    r = 10
    ---------
    m = 6
    l = 7
    r = 7
    ---------
    m = 7
    l = 8
    r = 7
    ---------
    """
    assert solution2(A=10, B=21) == 7
    assert solution2(A=13, B=11) == 5
    assert solution2(A=2, B=1) == 0
    assert solution2(A=1, B=8) == 2


def test_solution3():
    assert solution3([1, 2, 3, 4], [3, 3, 3, 7]) == 4
    assert solution3([2, 2, 2, 2, 2, 2], [7, 4, 2, 5, 1, 2]) == 4


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["2", "3", "+"], 5),
        (["2", "1", "+", "3", "*"], 9),
    ],
    ids=[
        "2 + 3",
        "(2 + 1) * 3",
    ],
)
def test_reverse_polish_notation(tokens, expected):
    actual = reverse_polish_notation(tokens=tokens)

    assert actual == expected
