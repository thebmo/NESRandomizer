from django import forms
from django.core.exceptions import ValidationError

from .models import NewsPost

class NewsPostForm(forms.ModelForm):

    class Meta:
        model = NewsPost
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'required': 'true'}),
            'body' : forms.Textarea(attrs={'rows':10, 'cols':85, 'name':'body'}),
            }
    
    def __init__(self, *args, **kwargs):
        return super(NewsPostForm, self).__init__(*args, **kwargs)