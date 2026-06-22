from django import forms
from .models import Post

class Postcreateform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image']
