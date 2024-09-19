from django.shortcuts import render

# Create your views here.
def festivals(request):
    return render(request, 'festival.html')