import os, sys

activate_this = 'C:/dev/virtualenvs/soe/Scripts/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

sys.path.append('C:/dev/django')
os.environ['DJANGO_SETTINGS_MODULE'] = 'soe.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()