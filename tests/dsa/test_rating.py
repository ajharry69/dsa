import pytest

from dsa.rating import get_ratings


@pytest.mark.parametrize(
    "rating, expected",
    [
        ("4.45", "full full full full half"),
        ("4.5", "full full full full half"),
        ("4.6", "full full full full full"),
        ("0.38", "half empty empty empty empty"),
        ("3.5", "full full full half empty"),
        ("3.51", "full full full full empty"),
        ("3.49", "full full full half empty"),
        ("-1", "empty empty empty empty empty"),
        ("0", "empty empty empty empty empty"),
    ],
)
def test_ratings(rating, expected):
    actual = get_ratings(rating=rating)

    assert actual == expected
