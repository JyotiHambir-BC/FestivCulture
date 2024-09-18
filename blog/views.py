from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.
class AllFestivals(generic.ListView):
    """
    Display the blogs in list on festival page.
    """
    queryset = Post.objects.all().filter(status=1)
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
        "festival.html",
        {"post": post,
        "comments": comments,
        "comments_count": comment_count,
        "comment_form": comment_form,
        },
        
    )

def comment_edit(request, slug, comment_id):
        if request.method == "POST":
            queryset = Post.objects.filter(status=1)
            post = get_object_or_404(queryset, slug=slug)
            comment = get_object_or_404(Comment, pk=comment_id)
            comment_form = CommentForm(data=request.POST, instance=comment)

            if comment_form.is_valid() and comment.author == request.user:
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.approved = False
                comment.save()
                messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
            else:
                messages.add_message(request, messages.ERROR, 'Error Updating Comments')

        return HttpResponseRedirect(reverse('details_post', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    
    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('details_post', args=[slug]))

