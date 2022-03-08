from .settings import *
from decouple import config

if os.path.exists('env.py'):
    import env
    
SECRET_KEY = os.environ.get("SECRET_KEY_PRODUCTION")
DEBUG = os.environ.get("DEBUG_PRODUCTION")

# ALLOWED_HOSTS
ALLOWED_HOSTS=['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}