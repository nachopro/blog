from settings.base import *  # noqa


DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': root_join('..', 'var', 'db.sqlite3')  # noqa
}
