from django.shortcuts import render
from django.contrib import messages
from .models import About

# Create your views here.


def about(request):
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request, "about.html",
        {
            "about": about,
        },
    )
