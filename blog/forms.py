
from django import forms
from django.contrib.auth.models import User
from .models import Post

class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ( 'username','email', 'password1', )

class PostForm(forms.ModelForm):

    class Meta:
        model= Post
        fields = ( 'title', 'text',)
