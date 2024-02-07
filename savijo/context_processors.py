from main.models import Service

def services(request):
    services = Service.objects.filter(active=True)
    return {"services": services}
