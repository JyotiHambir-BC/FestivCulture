from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.
class AllFestivals(generic.ListView):
    """
    Display the blogs in list on festival page.
    """
    queryset = Post.objects.all()
    template_name = "festival.html"
    paginate_by = 6

def details_post(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, 
                'Comment submitted and waiting for approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        
    )

