import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
class TestUserModel:
    @pytest.mark.parametrize(
        "email, phone_number",
        (
                ("user.1@example.org", None),
                (None, "+254712345678"),
                ("user.1@example.org", "+254712345678"),
        ),
    )
    def test_create_user(self, email, phone_number):
        user = User.objects.create_user(
            email=email,
            phone_number=phone_number,
            password="random password",
        )

        assert user.email == email
        assert user.phone_number == phone_number
        assert user.is_active
        assert not user.is_superuser

    @pytest.mark.parametrize(
        "email, phone_number",
        (
                ("user.1@example.org", None),
                (None, "+254712345678"),
                ("user.1@example.org", "+254712345678"),
        ),
    )
    def test_create_superuser(self, email, phone_number):
        user = User.objects.create_superuser(
            email=email,
            phone_number=phone_number,
            password="random password",
        )

        assert user.email == email
        assert user.phone_number == phone_number
        assert user.is_active
        assert user.is_superuser

    @pytest.mark.parametrize(
        "email, phone_number, natural_key",
        (
                ("user.1@example.org", None, "user.1@example.org"),
                (None, "+254712345678", "+254712345678"),
                ("user.1@example.org", "+254712345678", "user.1@example.org"),
                ("user.1@example.org", "+254712345678", "+254712345678"),
        ),
    )
    def test_get_by_natural_key(self, email, phone_number, natural_key):
        user = User.objects.create_user(
            email=email,
            phone_number=phone_number,
            password="random password",
        )

        authenticated_user = User.objects.get_by_natural_key(
            natural_key,
        )

        assert authenticated_user == user
        assert authenticated_user.email == user.email
        assert authenticated_user.phone_number == user.phone_number

    @pytest.mark.parametrize(
        "email, phone_number, natural_key",
        (
                ("user.1@example.org", None, "unexisting.user.1@example.org"),
                (None, "+254712345678", "+255712345678"),
                ("user.1@example.org", "+254712345678", "unexisting.user.1@example.org"),
                ("user.1@example.org", "+254712345678", "+256712345678"),
        ),
    )
    def test_get_by_natural_key_for_unexisting_key(self, email, phone_number, natural_key):
        User.objects.create_user(
            email=email,
            phone_number=phone_number,
            password="random password",
        )

        with pytest.raises(User.DoesNotExist):
            User.objects.get_by_natural_key(
                natural_key,
            )
