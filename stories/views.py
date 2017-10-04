from django.shortcuts import render
from .models import Article
from random import choice

# Create your views here.
def index(request):
    art = choice(list(Article.objects.all()))
    return render(request, 'stories/index.html', {'art': art})
