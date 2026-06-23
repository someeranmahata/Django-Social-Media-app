from django.db import models
from django.contrib.auth.models import User
from userProfile.models import Profile
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True,null=True)
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comment'
    )
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='comment'
    )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]
        
    def __str__(self):
        return f"commented by {self.user} on {self.created}"
    