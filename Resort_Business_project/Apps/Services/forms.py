from django import forms
from .models import Comments
from ..Authentication.models import User


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('message',)
        error_messages = {
            'message': {
                'required': "Please Enter your Comment before you post."
            },
        }
        widgets = {
            'message': forms.TextInput(
                attrs={'class': 'form', 'placeholder': 'Comment Your Comment', 'required': True})
        }
        labels = {
            'message': '',
        }
