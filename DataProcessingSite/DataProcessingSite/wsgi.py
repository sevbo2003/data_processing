"""
WSGI config for DataProcessingSite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import dotenv
from django.core.wsgi import get_wsgi_application


d_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
dotenv.load_dotenv(
    d_file
)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataProcessingSite.settings.staging')

if os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = os.getenv('DJANGO_SETTINGS_MODULE')

application = get_wsgi_application()