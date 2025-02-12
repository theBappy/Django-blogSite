from django import forms
from .models import BlogPost
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost 
        fields = ['title', 'content', 'author'] 

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields  = ['username', 'email', 'password1', 'password2'] 


