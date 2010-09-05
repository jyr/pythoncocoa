import os, sys
sys.path.append('/home/pythonco/public_html/modules')
sys.path.append('/home/pythonco/public_html/modules/django')
sys.path.append('/home/pythonco/public_html/pythoncocoa')
sys.path.append('/home/pythonco/public_html')
sys.path.append('/home/pythonco/public_html/modules/django_cms-2.0.2-py2.6.egg')
os.environ['DJANGO_SETTINGS_MODULE'] = 'pythoncocoa.settings'
os.environ['PYTHON_EGG_CACHE'] = '/tmp/trac-eggs'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
