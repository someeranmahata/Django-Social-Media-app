from django import forms
from .models import Post,Comment

class Postcreateform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image']
class commentcreateform(forms.ModelForm): 
    class Meta: 
        model = Comment 
        fields = ['body']