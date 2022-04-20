from django import forms
from .models import Comments
from ..Authentication.models import User


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('message',)
        error_messages = {
            'message': {
                'required': "Please Enter your Comment.",
            },
        }
        widgets = {
            'message': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Comment Your Review', 'required': True},)
        }

