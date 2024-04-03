from settings.base import *  # noqa


DATABASES['default'] = {  # noqa
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': root_join('..', 'db.sqlite3')  # noqa
}
