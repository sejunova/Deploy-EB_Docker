import logging
import random
import string

from .base import *

logger = logging.getLogger(__name__)
ALLOWED_HOSTS = [
    '.elasticbeanstalk.com',
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECRET_KEY = ''.join([random.choice(string.ascii_lowercase) for i in range(40)])

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(ROOT_DIR, '.log', 'django.log')
        },
        'sentry':{
            'level':'ERROR',
            'class':'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file', 'sentry'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

DEBUG = False
