from django.shortcuts import render
from .models import ScrapedData

def index(request):
    scraped_data = ScrapedData.objects.all()
    return render(request, 'index.html', {'scraped_data': scraped_data})
