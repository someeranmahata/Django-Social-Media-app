from django.contrib import admin
from .models import Post, Comment
# Register your models here.

admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','body', 'created','image', 'updated']
    search_fields = ['title', 'author']
    
admin.site.register(Comment)
class CommentAdmin:
    list_display = ['body', 'created', 'updated']
    search_fields = ['comment', 'post']
