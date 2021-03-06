import os
import sys
import site
 
# One directory above the project, so project name will be needed for imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
 
# with mod_wsgi >= 2.4, this line will add this path in front of the python path
site.addsitedir(os.path.join(root_dir, 'oppian-env/lib/python2.5/site-packages'))
 
# add this django project
sys.path.append(root_dir)
sys.path.append(os.path.join(root_dir, 'oppian-env/lib/python2.5/site-packages'))
sys.path.append(os.path.join(root_dir, '..'))
sys.path.append(os.path.join(root_dir, 'lib/django'))
sys.path.append(os.path.join(root_dir, 'apps'))
sys.path.append(os.path.join(root_dir, 'apps/oppianapp/utils'))
sys.path.append(os.path.join(root_dir, 'lib/django-storages'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


import django.core.handlers.wsgi
 
application = django.core.handlers.wsgi.WSGIHandler()
