from .defaults import *

# Pagination
STUDENTS_PER_PAGE   = 200
COURSES_PER_PAGE    = 10
EXAMS_PER_PAGE      = 10

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = open(os.path.expanduser('~/.pyclassbook_secret')).read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'pyclassbook.sqlite3'),
    }
}

# INTERNATIONALIZATION
LANGUAGE_CODE = "fr"
TIME_ZONE = 'Europe/Paris'