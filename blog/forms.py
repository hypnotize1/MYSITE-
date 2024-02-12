from django import forms
from blog.models import Comment
from captcha.fields import CaptchaField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['Post', 'name', 'subject', 'message', 'email']