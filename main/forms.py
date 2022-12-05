from django import forms

from .models import News


class NewsAddForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ('title', 'text', 'image')
