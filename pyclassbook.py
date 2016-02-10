#!/usr/bin/env python3
import os
import sys
from subprocess import call

if __name__ == "__main__":
    
    if sys.argv[1] == "dev":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyclassbook.settings.dev")
    elif sys.argv[1] == "prod":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyclassbook.settings.prod")
    elif sys.argv[1] == "live":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyclassbook.settings.live")
    elif sys.argv[1] == "key":
        from django.utils.crypto import get_random_string
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        print(get_random_string(50, chars))
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyclassbook.settings")
        

call(["./manage.py", "runserver"])