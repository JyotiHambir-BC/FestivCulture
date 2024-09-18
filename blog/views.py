from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse
from .models import Post, Comment
# from .forms import CommentForm

# Create your views here.
class AllFestivals(generic.ListView):
    """
    Display the blogs in list on festival page.
    """
    queryset = Post.objects.all()
    template_name = "festival.html"
    paginate_by = 6
