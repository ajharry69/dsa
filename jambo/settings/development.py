from .base import *  # noqa

DEBUG = True

SECRET_KEY = "django-insecure-k_4puq09t7f=h9x8ozy9cxb2@+%6bm9tyjlj7r89co)1jy)yib"

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE

INTERNAL_IPS = type(str("c"), (), {"__contains__": lambda *a: True})()

try:
    from .local import *  # noqa
except ImportError:
    pass
