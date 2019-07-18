from django import forms
from .models impost *

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('author','text')
    def clean_author(self):
        value=self.cleaned_data['author']
        if len(value) > 5:
            return value
        raise forms.ValidationError('Author need to be more than 5 chars')
