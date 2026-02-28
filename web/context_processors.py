from .models import SiteSettings, Partner

def site_context(request):
    settings = SiteSettings.objects.first()
    partners = Partner.objects.all()
    return {
        'site_settings': settings,
        'all_partners': partners,
    }
