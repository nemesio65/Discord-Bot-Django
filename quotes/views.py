from django.shortcuts import render
from .models import Quote

# Create your views here.
def quotes(request):
    quotes = Quote.objects.all().values('series', 'quote', 'character')
    return render(request, 'quotes/quotes.html', {'quotes':quotes})

