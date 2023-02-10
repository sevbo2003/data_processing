from DataProcessingSite.settings.base import *

DEBUG = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


# Media files (CSS, JavaScript, Images)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')



# Set the allowed hosts based on the environment.
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")
