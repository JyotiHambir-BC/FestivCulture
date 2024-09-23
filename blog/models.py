from django.db import models
from django import forms
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Post(models.Model):
    """
    Stores a single blog post entry related to :model: `auth.user`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="blogpost_likes", blank=True)
    comment_count = models.IntegerField(default=0)
    best_time = models.CharField(max_length=100, verbose_name="Best time(month/season)")
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ["-created_on", "author"]
    
    def __str__(self):
        return f"{self.title} | written by {self.author}"
    
    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    """
    Stores a single blog's comment add request. 
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)
  
    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"Comment {self.body} by {self.author}"

class Reviews(models.Model):
    """
    Stores a review of blogs.
    """
    CHOICES = [('Y','Yes'),('N','No')]

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reviews")
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviewer")
    review = models.TextField()
    like = forms.CharField(label='Like', widget=forms.RadioSelect(choices=CHOICES))
    created_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"Review: {self.review} by {self.name}"