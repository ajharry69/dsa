import datetime
from datetime import timedelta

import pytest
from django.core.exceptions import ValidationError

from jambo.apps.customers.models import past_date_validator
from tests.factories import BusinessFactory


@pytest.mark.parametrize(
    "date",
    [
        datetime.date.today(),
        datetime.date.today() - timedelta(days=1),
    ],
    ids=["today", "past-date"],
)
def test_past_date_validator_for_valid_dates(date):
    actual = past_date_validator(date)

    assert actual is None


def test_past_date_validator_for_invalid_date():
    with pytest.raises(ValidationError, match=r"Date cannot be after than .*"):
        past_date_validator(datetime.date.today() + timedelta(days=1))


@pytest.mark.django_db
class TestBusiness:
    @pytest.mark.parametrize(
        "registration_date,expected_output",
        [
            (datetime.date.today(), 0),
            (datetime.date.today() - timedelta(days=1), 1),
            (datetime.date.today() - timedelta(days=1_000), 1_000),
        ],
    )
    def test_age_in_days(self, registration_date, expected_output):
        business = BusinessFactory(registration_date=registration_date)

        actual = business.age_in_days

        assert actual == expected_output
