import os, sys, site

root = os.path.dirname(os.path.abspath(__file__))

site.addsitedir(os.path.join(root, '../lib/python2.6/site-packages'))
sys.path = [os.path.dirname(root), root] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
