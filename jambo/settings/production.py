from .base import *  # noqa

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

DEBUG = False

ALLOWED_HOSTS = []

try:
    from .local import *  # noqa
except ImportError:
    pass
