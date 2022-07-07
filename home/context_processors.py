from .models import HomePage

def linkItems(request):
    
    return {'HomePageIndex': HomePage.objects.all().order_by('pk')[1:],'websitetitle': HomePage.objects.first(),}