from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Favourite, Author


# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'updated_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Add fields for author in admin panel
    """

    list_display = ("user", "created_on", "email", "approved")
    search_fields = ["user"]


admin.site.register(Favourite)

admin.site.register(Comment)
