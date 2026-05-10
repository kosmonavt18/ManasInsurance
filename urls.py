from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),  # переключатель языка
]

urlpatterns += i18n_patterns(
    path('', include('apps.core.urls', namespace='core')),
    path('accounts/', include('apps.accounts.urls', namespace='accounts')),
    path('clients/', include('apps.clients.urls', namespace='clients')),
    path('corporate/', include('apps.corporate.urls', namespace='corporate')),
    path('auto/', include('apps.auto.urls', namespace='auto')),
    path('applications/', include('apps.applications.urls', namespace='applications')),
    path('calculators/', include('apps.calculators.urls', namespace='calculators')),
    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
