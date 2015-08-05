# -*- coding: utf-8 -*-
import os
import sys

if os.environ.get('SERVER_SOFTWARE','').startswith('Dev'):
    sys.path.append('/usr/local/google_appengine/lib/django-1.5/')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo.settings")
