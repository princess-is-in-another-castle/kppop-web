from django.shortcuts import render
from .models import Article


# Create your views here.
def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all(), 'STATIC_URL': 'static/'})
