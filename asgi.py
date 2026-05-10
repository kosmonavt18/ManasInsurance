import os
from django.core.asgi import get_asgi_application

# settings.py находится в корне проекта рядом с manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
application = get_asgi_application()
