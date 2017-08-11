from django import forms
from django.forms import ModelForm
from .models import Comment

class CommentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Comment
        fields = ('user','password','content')
