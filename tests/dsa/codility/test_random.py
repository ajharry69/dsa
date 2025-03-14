from decimal import Decimal as D

import pytest

from dsa.codility.random import (
    solution,
    reposition_zeros,
    move_zeros,
    get_triangle_type,
    is_leap_year,
    calculate_discount,
    CountInstance,
    split,
    replace_char_with_position,
    count_smileys,
    highest_scoring_word,
    highest_scoring_word_1,
    delete_nth_while_retaining_position,
    first_non_repeating_letter,
)


def test_instance_count():
    CountInstance()
    CountInstance()
    CountInstance()

    # noinspection PyUnresolvedReferences
    assert CountInstance.instance_count == CountInstance.instance_count_meta == 3


def test_solution():
    assert solution(images=list(range(1, 7))) == [
        (1, "I"),
        (2, "P1"),
        (3, "P2"),
        (4, "I"),
        (5, "P1"),
        (6, "P2"),
    ]


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 3, 0, 12, 0], [3, 12, 0, 0, 0]),
        ([-1, 0, 3, 0, 0, 12, 0], [-1, 3, 12, 0, 0, 0, 0]),
    ],
)
def test_reposition_zeros(nums, expected):
    actual = reposition_zeros(nums=nums)

    assert actual == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 3, 0, 12, 0], [3, 12, 0, 0, 0]),
        ([-1, 0, 3, 0, 0, 12, 0], [-1, 3, 12, 0, 0, 0, 0]),
    ],
)
def test_move_zeros(nums, expected):
    actual = move_zeros(nums=nums)

    assert actual == expected


@pytest.mark.parametrize(
    "length1, length2, length3, expected",
    [
        (0, 0, 0, "Impossible"),
        (0, -1, 0, "Impossible"),
        (1, 2, 3, "Scalene"),
        (1, 2, 2, "Isosceles"),
        (2, 2, 2, "Equilateral"),
    ],
)
def test_get_triangle_type(length1, length2, length3, expected):
    actual = get_triangle_type(length1, length2, length3)

    assert actual == expected


@pytest.mark.parametrize(
    "year, expected",
    [
        (1996, True),
        (1998, False),
        (2000, True),
        (2001, False),
        (2002, False),
        (2003, False),
        (2004, True),
        (2020, True),
        (2022, False),
        (2024, True),
        (1584, True),
        (1588, True),
        (1592, True),
        (1596, True),
        (1600, True),
        (1604, True),
        (1608, True),
        (1612, True),
        (1616, True),
        (1620, True),
        (1624, True),
        (1628, True),
        (1632, True),
        (1636, True),
        (1640, True),
        (1644, True),
        (1648, True),
        (1652, True),
        (1656, True),
        (1660, True),
        (1664, True),
        (1668, True),
        (1672, True),
        (1676, True),
        (1680, True),
        (1684, True),
        (1688, True),
        (1692, True),
        (1696, True),
        (1704, True),
        (1708, True),
        (1712, True),
        (1716, True),
        (1720, True),
        (1724, True),
        (1728, True),
        (1732, True),
        (1736, True),
        (1740, True),
        (1744, True),
        (1748, True),
        (1752, True),
        (1756, True),
        (1760, True),
        (1764, True),
        (1768, True),
        (1772, True),
        (1776, True),
        (1780, True),
        (1784, True),
        (1788, True),
        (1792, True),
        (1796, True),
        (1804, True),
        (1808, True),
        (1812, True),
        (1816, True),
        (1820, True),
        (1824, True),
        (1828, True),
        (1832, True),
        (1836, True),
        (1840, True),
        (1844, True),
        (1848, True),
        (1852, True),
        (1856, True),
        (1860, True),
        (1864, True),
        (1868, True),
        (1872, True),
        (1876, True),
        (1880, True),
        (1884, True),
        (1888, True),
        (1892, True),
        (1896, True),
        (1904, True),
        (1908, True),
        (1912, True),
        (1916, True),
        (1920, True),
        (1924, True),
        (1928, True),
        (1932, True),
        (1936, True),
        (1940, True),
        (1944, True),
        (1948, True),
        (1952, True),
        (1956, True),
        (1960, True),
        (1964, True),
        (1968, True),
        (1972, True),
        (1976, True),
        (1980, True),
        (1984, True),
        (1988, True),
        (1992, True),
        (1996, True),
        (2000, True),
        (2004, True),
        (2008, True),
        (2012, True),
        (2016, True),
        (2020, True),
        (2024, True),
        (2028, True),
        (2100, False),
    ],
)
def test_is_leap_year(year, expected):
    actual = is_leap_year(year)

    assert actual is expected


@pytest.mark.parametrize(
    "amount, is_member, expected",
    [
        (100, False, 100),
        (100, True, 95),
        (150, False, 135),
        (150, True, 128.25),
        (300, True, D("243.67")),
    ],
)
def test_calculate_discount(amount, is_member, expected):
    actual = calculate_discount(
        amount=amount,
        is_member=is_member,
    )

    assert actual == expected


@pytest.mark.parametrize(
    "data, sep, maxsplit",
    [
        ("", None, -1),
        ("example", None, -1),
        (" example", None, -1),
        ("     example", None, -1),
        ("example    ", None, -1),
        ("              example    ", None, -1),
        ("example test", None, -1),
        ("example  test", None, -1),
        ("example       test", None, -1),
        ("", " ", -1),
        ("example", " ", -1),
        (" example", " ", -1),
        ("     example", " ", -1),
        ("example    ", " ", -1),
        ("              example    ", " ", -1),
        ("example test", " ", -1),
        ("example  test", " ", -1),
        ("example       test", " ", -1),
        ("exampletest", "test", -1),
        ("testexample", "test", -1),
        ("example       test", "test", -1),
        ("example       test    ", "test", -1),
        ("example       test  x test ", "test", -1),
        ("testexample       test  x test ", "test", -1),
        ("test>example       test  x test ", "test", -1),
        ("example       test  x test ", "test", 0),
        ("example       test  x test ", "test", 1),
        ("example       test  x test ", "test", 2),
        ("a,,b", ",", -1),
        (",hello", ",", -1),
        ("abab", "ab", -1),
        ("abab", "ab", 1),
    ],
)
def test_split(data, sep, maxsplit):
    actual = split(data=data, sep=sep, maxsplit=maxsplit)
    assert actual == data.split(sep=sep, maxsplit=maxsplit)


@pytest.mark.parametrize(
    "data, sep, maxsplit",
    [
        ("", "", -1),
        ("example", "", -1),
        (" example", "", -1),
        ("     example", "", -1),
        ("example    ", "", -1),
        ("              example    ", "", -1),
        ("example test", "", -1),
        ("example  test", "", -1),
        ("example       test", "", -1),
    ],
)
def test_split_should_raise_ValueError(data, sep, maxsplit):
    with pytest.raises(ValueError):
        split(data=data, sep=sep, maxsplit=maxsplit)

    with pytest.raises(ValueError):
        data.split(sep=sep, maxsplit=maxsplit)


@pytest.mark.parametrize(
    "string, expected",
    [
        (
            "The sunset sets at twelve o' clock.",
            "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11",
        ),
    ],
)
def test_replace_char_with_position(string, expected):
    actual = replace_char_with_position(string=string)

    assert actual == expected


@pytest.mark.parametrize(
    "smiles,expected",
    [
        ([":)", ";(", ";}", ":- D"], 1),
        ([":)", ";(", ";}", ":-D"], 2),
        ([";D", ":-(", ":-)", ";~)"], 3),
        ([";]", ":[", ";*", ":$", ";-D"], 1),
    ],
)
def test_count_smileys(smiles, expected):
    actual = count_smileys(smiles=smiles)

    assert actual == expected


__test_cases_highest_scoring_word = [
    ("", ""),
    ("example", "example"),
    ("aaaa abad", "abad"),
    ("aaaZ abad", "aaaZ"),
    ("man i need a taxi up to ubud", "taxi"),
    ("what time are we climbing up the volcano", "volcano"),
    ("take me to semynak", "semynak"),
    ("aa b", "aa"),
    ("b aa", "b"),
    ("bb d", "bb"),
    ("d bb", "d"),
    ("aaa b", "aaa"),
]


@pytest.mark.parametrize(
    "words, expected",
    __test_cases_highest_scoring_word,
)
def test_highest_scoring_word(words, expected):
    actual = highest_scoring_word(words=words)

    assert actual == expected


@pytest.mark.parametrize(
    "words, expected",
    __test_cases_highest_scoring_word,
)
def test_highest_scoring_word_1(words, expected):
    actual = highest_scoring_word_1(words=words)

    assert actual == expected


@pytest.mark.parametrize(
    "nums, max_appearances, expected",
    [
        ([20, 37, 20, 21], 1, [20, 37, 21]),
        ([1, 1, 3, 3, 7, 2, 2, 2, 2], 3, [1, 1, 3, 3, 7, 2, 2, 2]),
        ([12, 39, 19, 39, 39, 19, 12], 1, [12, 39, 19]),
        ([1, 2, 3, 1, 2, 1, 2, 3], 2, [1, 2, 3, 1, 2, 3]),
    ],
)
def test_delete_nth_while_retaining_position(nums, max_appearances, expected):
    actual = delete_nth_while_retaining_position(
        nums=nums,
        max_appearances=max_appearances,
    )

    assert actual == expected


@pytest.mark.parametrize(
    "string, expected",
    [
        ("", ""),
        ("tt", ""),
        ("stress", "t"),
        ("sTreSS", "T"),
        ("moonmen", "e"),
    ],
)
def test_first_non_repeating_letter(string, expected):
    actual = first_non_repeating_letter(string=string)

    assert actual == expected
