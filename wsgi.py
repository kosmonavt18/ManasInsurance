import os
from django.core.wsgi import get_wsgi_application

# settings.py находится в корне проекта рядом с manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
application = get_wsgi_application()
