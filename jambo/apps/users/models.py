import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from jambo.apps.users.managers import UserManager


class User(AbstractUser):
    username = models.CharField(_("Username"), max_length=150, default=uuid.uuid4, unique=True)
    phone_number = models.CharField(_("Phone number"), max_length=20, db_index=True, null=True)
    email = models.EmailField(_("Email address"), max_length=150, db_index=True, null=True)

    REQUIRED_FIELDS = AbstractUser.REQUIRED_FIELDS + ["phone_number"]

    objects = UserManager()

    class Meta:
        swappable = "AUTH_USER_MODEL"
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        unique_together = (
            ("phone_number", "email"),
        )
