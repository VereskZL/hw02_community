from django import forms
from .models import PostForm


class PostForm(forms.ModelForm):
    class Meta:
        model = PostForm
        fields = ('text', 'group')

    def clean_subject(self):
        data = self.cleaned_data['text']

        if '' in data.lower():
            raise forms.ValidationError('А что читать то?')
        return data
