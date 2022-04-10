from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ['category' ,'title', 'description', 'thumbnail', 'content']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["content"]