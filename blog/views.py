from django.shortcuts import render

from .models import Article

def home(request):
    articles = Article.objects.all()
    return render(request, 'myapp/home.html', {'articles': articles})