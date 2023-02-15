"""
ASGI config for DataProcessingSite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import dotenv
from django.core.asgi import get_asgi_application


d_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
dotenv.load_dotenv(
    d_file
)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataProcessingSite.settings.local')

if os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = os.getenv('DJANGO_SETTINGS_MODULE')

application = get_asgi_application()
