from django.shortcuts import render
from blog.models import Post

# Create your views here.


def festivals(request):
    return render(request, 'festival.html')
