from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment, Favourite
from .forms import CommentForm

# Create your views here.
class AllFestivals(generic.ListView):
    """
    Display the blogs in list on festival page.
    """
    queryset = Post.objects.filter(status=1)
    template_name = "festival.html"
    paginate_by = 6

def details_post(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    is_favourite = False

    if post.favourite_post.filter(id=request.user.id):
        is_favourite = True

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
        "details_post.html",
        {"post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        "is_favourite": is_favourite,
               
        },
        
    )

def comment_edit(request, slug, comment_id):
    """
    Edit the single comment which have already submitted.
    """
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

    return HttpResponseRedirect(reverse("details_post", args=[slug]))

class PostLike(View):
    """
    When a post is liked/unliked, the slug is noted
    and the like/unlike is counted. Total likes display
    """

    def post(self, request, slug, *args):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=self.request.user.id).exists():
            post.likes.remove(request.user)
            messages.success(request, "You have unliked this post.")
        else:
            post.likes.add(request.user)
            messages.success(request, "You have liked this post, Thanks!")
        return HttpResponseRedirect(reverse("details_post", args=[slug]))


def favourite_list(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if post.favourite_post.filter(id=request.user.id).exists():
        post.favourite_post.remove(request.user)
        messages.success(request, "You have removed this Post from your Favourite List.")
    else:
        post.favourite_post.add(request.user)
        messages.success(request, "You have added this Post in your Favourite List.")

    return HttpResponseRedirect(reverse("details_post", args=[slug]))


def view_favourite_list(request):
    """
    View all selected favourite posts in favourite list on different page
    """
    user = request.user
    favourite_lists = user.favourite_post.all()
    context = {
        "favourite_lists": favourite_lists,
    }
    return render(request, "favourite_list.html", context)






   