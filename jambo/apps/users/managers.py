from django.contrib.auth.models import UserManager as BaseUserManager
from django.db.models import Q


class UserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        return self.filter(
            Q(username=username)
            | Q(email=username)
            | Q(phone_number=username)
        ).get()
