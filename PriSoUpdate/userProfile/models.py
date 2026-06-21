from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    profile_pic=models.ImageField(
        upload_to='profile-pic/',
        default="default.jpg" 
    )
    bio=models.TextField(max_length=250)
    created=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']
    def __str__(self):
        return self.user.username

