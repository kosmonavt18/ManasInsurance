from .models import SiteSettings


def site_settings(request):
    """Делает settings сайта доступными во всех шаблонах как {{ site }}."""
    return {'site': SiteSettings.load()}
