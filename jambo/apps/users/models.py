import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from jambo.apps.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, default=uuid.uuid4, unique=True)
    phone_number = models.CharField(max_length=20, db_index=True, null=True)
    email = models.EmailField(max_length=150, db_index=True, null=True)
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"  # returned by get_email_field_name()

    REQUIRED_FIELDS = [EMAIL_FIELD, "phone_number"]

    objects = UserManager()

    class Meta:
        swappable = "AUTH_USER_MODEL"
        unique_together = (
            ("phone_number", "email"),
        )
