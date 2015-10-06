import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

prj_path = os.path.abspath(os.path.join(__file__, '../..'))

if prj_path not in sys.path:
    sys.path.append(prj_path)
