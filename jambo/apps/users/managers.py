from django.contrib.auth.base_user import BaseUserManager
from django.db.models import Q


class UserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        return self.filter(
            Q(username=username)
            | Q(email=username)
            | Q(phone_number=username)
        ).get()

    def create_user(self, **kwargs):
        commit = kwargs.pop("save_record", True)
        password = kwargs.pop("password", None)

        # username = self.model.normalize_username(username)
        # kwargs[self.model.USERNAME_FIELD] = username

        email_field_name = self.model.get_email_field_name()
        email = kwargs.get(email_field_name)
        if email is not None:
            kwargs[email_field_name] = self.normalize_email(email)

        user = self.model(**kwargs)
        user.set_password(password)
        if commit:
            user.save(using=self._db)
        return user

    def create_superuser(self, password, **kwargs):
        if not password:
            raise ValueError("superuser password is required")

        commit = kwargs.pop("save_record", True)
        user = self.create_user(password=password, save_record=False, **kwargs)
        user.is_superuser = True
        if commit:
            user.save(using=self._db)
        return user
